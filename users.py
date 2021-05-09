from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, request
import os

def login(username, password):
	sql = "SELECT password, id, admin FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if user == None:
		#invalid username
		return False
	else:
		hash_value = user[0]
		if check_password_hash(hash_value, password):
			session["username"] = username
			session["user_id"] = user[1]
			session["user_role"] = user[2]
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
		sql = """INSERT INTO users (username, password,admin) 
		VALUES (:username, :password, False)"""
		db.session.execute(sql, {"username":username, "password":hash_value})
		db.session.commit()
	except:
		return False
	return login(username,password)

def username_exists_already(username):
	sql = "SELECT id from users where username=:username"
	result = db.session.execute(sql, {"username":username})
	exists = result.fetchone()
	if exists == None:
		return False
	return True

def require_admin():
	if session["user_role"] == False:
		abort(403)

def check_csrf():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

def list_admins():
	sql = "Select username from users where admin=True ORDER BY username"
	result = db.session.execute(sql)
	admins = result.fetchall()
	return admins

def turn_user_into_admin(username):
	try:
		sql = "UPDATE users SET admin=True WHERE username=:username"
		db.session.execute(sql, {"username":username})
		db.session.commit()
	except:
		return False
	return True


def get_number_of_admins():
	sql = "Select count(*) from users where admin=True"
	result = db.session.execute(sql)
	number_of_admins = result.fetchone()[0]
	if number_of_admins != None:
		return number_of_admins
	else:
		return 0

def check_if_admin(username):
	sql = "Select admin from users where username=:username"
	result = db.session.execute(sql, {"username":username})
	is_admin = result.fetchone()
	if is_admin == None:
		return False
	return bool(is_admin[0])