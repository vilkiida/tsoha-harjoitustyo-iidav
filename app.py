from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def main():
	return render_template("main.html")

@app.route("/login", methods=["POST"])
def login():
	username= request.form["username"]
	password= request.form["password"]

	sql = "SELECT password FROM users WHERE username=:username"
	result=db.session.execute(sql, {"username":username})
	user=result.fetchone()
	if user == None:
		#invalid username
		return redirect("/")
	else:
		hash_value = user[0]
		if check_password_hash(hash_value, password):
			session["username"] = username
			return redirect("/")
		else:
			#invalid password
			return redirect("/")

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

@app.route("/make_account")
def make_account():
	return render_template("make_account.html")

@app.route("/new_account", methods=["POST"])
def new_account():
	username= request.form["username"]
	password= request.form["password"]
	hash_value = generate_password_hash(password)
	sql = "INSERT INTO users (username, password,admin) VALUES (:username, :password, False)"
	db.session.execute(sql, {"username":username, "password":hash_value})
	db.session.commit()
	return render_template("new_account.html")
