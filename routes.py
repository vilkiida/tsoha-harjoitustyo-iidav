from app import app
import movies
import users
#import reviews
from flask import redirect, render_template, request

@app.route("/", methods = ["GET"])
def main():
	movie_list = movies.get_movie_list()
	return render_template("main.html", movies=movie_list)

@app.route("/login", methods=["POST"])
def login():
    username=request.form["username"]
    password=request.form["password"]
    if users.login(username,password) == True:
        return redirect("/")
    else:
        return render_template("login_issue.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/make_account")
def make_account():
    return render_template("make_account.html")

@app.route("/new_account", methods=["POST"])
def new_account():
    username = request.form["username"]
    password = request.form["password"]
    users.new_account(username,password)
    return render_template("new_account.html")

@app.route("/movie_page/<int:id>")
def movie_page(id):
    info = movies.get_movie_info(id)
    reviews = reviews.get_reviews(id)
    return render_template("movie_page.html", information=info,reviews=reviews)




