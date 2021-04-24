from app import app
import movies
import users
import reviews
import suggestions
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
    review_list = reviews.get_reviews(id)
    amount_of_reviews = reviews.get_amount(id)
    average= reviews.get_average(id)
    return render_template("movie_page.html", information=info,reviews=review_list, amount_of_reviews=amount_of_reviews, average=average)


@app.route("/new_review/<int:id>", methods=["POST"])
def new_review(id):
    movie_id=id
    grade = request.form["grade"]
    review = request.form["review"]
    reviews.create_review(movie_id, grade, review)
    return redirect("/movie_page/"+ str(id))

@app.route("/my_reviews")
def my_reviews():
    mine = reviews.get_my_reviews()
    number_of_reviews=reviews.get_number_of_reviews()
    return render_template("my_reviews.html", mine=mine, number_of_reviews=number_of_reviews)

@app.route("/suggest_movies")
def suggest_movies():
    return render_template("suggest_movies.html")

@app.route("/new_suggestion", methods=["POST"])
def new_suggestion():
    name=request.form["name"]
    year=request.form["year"]
    genres=request.form["genre"]
    description=request.form["description"]
    leading_roles=request.form["leading_roles"]
    suggestions.make_suggestion(name, year, genres, description, leading_roles)
    return render_template("new_suggestion.html")

@app.route("/add_movie")
def add_movie():
    return render_template("add_movie.html")

@app.route("/new_movie", methods=["POST"])
def new_movie():
    name=request.form["name"]
    year=request.form["year"]
    genres=request.form["genre"]
    description=request.form["description"]
    leading_roles=request.form["leading_roles"]
    movies.add_movie(name,year,genres,description,leading_roles)
    return render_template("new_movie.html")
