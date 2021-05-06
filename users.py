from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, request
import os

def login(username,password):
	sql = "SELECT password, id, admin FROM users WHERE username=:username"
	result=db.session.execute(sql, {"username":username})
	user=result.fetchone()
	if user == None:
		#invalid username
		return False
	else:
		hash_value = user[0]
		if check_password_hash(hash_value, password):
			session["username"] = username
			session["user_id"] = user[1]
			session["user_role"]=user[2]
			session["csrf_token"] = os.urandom(16).hex()
			return True
		else:
			#invalid password
			return False
    
def logout():
	del session["username"]
	del session["user_id"]
	del session["user_role"]

def register(username,password):
	try:
		hash_value = generate_password_hash(password)
		sql = "INSERT INTO users (username, password,admin) VALUES (:username, :password, False)"
		db.session.execute(sql, {"username":username, "password":hash_value})
		db.session.commit()
	except:
		return False
	return login(username,password)

def username_exists_already(username):
	sql="SELECT id from users where username=:username"
	result=db.session.execute(sql, {"username":username})
	exists=result.fetchone()
	if exists == None:
		return False
	return True

def require_admin():
	if session["user_role"] == False:
		abort(403)

def check_csrf():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)
