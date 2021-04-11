from flask import Flask
from flask import redirect, render_template, request, session
#from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
#db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def main():
	return render_template("main.html")

@app.route("/login", methods=["POST"])
def login():
	username= request.form["username"]
	password= request.form["password"]
	session["username"] = username
	return redirect("/")

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

