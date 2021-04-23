from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
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
			return True
		else:
			#invalid password
			return False
    
def logout():
	del session["username"]

def new_account(username,password):
	hash_value = generate_password_hash(password)
	sql = "INSERT INTO users (username, password,admin) VALUES (:username, :password, False)"
	db.session.execute(sql, {"username":username, "password":hash_value})
	db.session.commit()
