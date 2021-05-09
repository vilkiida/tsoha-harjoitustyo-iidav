from app import app
import movies
import users
import reviews
import suggestions
import categories
from flask import redirect, render_template, request

@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "GET":
	    movie_list = movies.get_movie_list()
	    return render_template("main.html", movies=movie_list)

    if request.method == "POST":
        sort=request.form.get("sort")
        if sort == "newest":
            movie_list=movies.get_movie_list_newest()
        elif sort == "oldest":
            movie_list=movies.get_movie_list_oldest()
        elif sort == "best":
            movie_list=movies.get_movie_list_best()
        elif sort == "worst":
            movie_list=movies.get_movie_list_worst()
        elif sort == "latest":
            movie_list = movies.get_movie_list()
        else:
            movie_list = movies.get_movie_list()
        return render_template("main.html", movies=movie_list)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("login_issue.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("make_account.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.username_exists_already(username):
            return render_template ("register_error.html", message="Käyttäjätunnus on varattu.")
        if len(username) >= 20 or len(username) <= 1:
            return render_template("register_error.html", message="Käyttäjätunnuksen täytyy olla 1-20 merkkiä.")
        if password == "":
            return render_template("register_error.html", message="Salasana on tyhjä.")
        
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("register_error.html", message="Uuden tunnuksen luonti epäonnistui.")

@app.route("/movie_page/<int:id>", methods=["GET", "POST"])
def movie_page(id):
    if request.method == "GET":
        if not movies.get_movie_info(id):
            return render_template("issue.html", message="Valitettavasti elokuvaa ei löytynyt.")
        info = movies.get_movie_info(id)
        review_list = reviews.get_reviews(id)
        amount_of_reviews = reviews.get_amount(id)
        average= reviews.get_average(id)
        return render_template("movie_page.html", information=info,reviews=review_list, amount_of_reviews=amount_of_reviews, average=average, id=id)
    if request.method == "POST":
        users.check_csrf()
        movie_id=request.form["movie_id"]
        grade = int(request.form["grade"])
        review = request.form["review"]
        if grade == 0 or grade == 1 or grade == 2 or grade == 3 or grade == 4 or grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10:
            if not reviews.create_review(movie_id, grade, review):
                return render_template("review_issue.html", message="Arvostelun lisäys ei onnistunut", id=id)
            else:
                return redirect("/movie_page/"+ str(movie_id))
        return render_template("review_issue.html", message="Arvostelussa pitää olla ainakin arvosana.", id=id)
        

@app.route("/my_reviews")
def my_reviews():
    mine = reviews.get_my_reviews()
    number_of_reviews = reviews.get_number_of_reviews()
    return render_template("my_reviews.html", mine=mine, number_of_reviews=number_of_reviews)

@app.route("/suggest_movies")
def suggest_movies():
    return render_template("suggest_movies.html")

@app.route("/new_suggestion", methods=["POST"])
def new_suggestion():
    users.check_csrf()
    name = request.form["name"]
    if len(name) < 1 or len(name) > 177:
        return render_template("suggestion_error.html", message="Elokuvan nimi pitää olla 1-177 merkkiä.")
    year=request.form["year"]
    if len(year) != 4:
        return render_template("suggestion_error.html", message="Vuosiluvussa pitää olla 4 numeroa")
    if int(year) > 2021:
        return render_template("suggestion_error.html", message="Julkaisu vuosi ei voi olla uudempi kuin 2021")
    genres=request.form["genre"]
    if genres == "":
        return render_template("suggestion_error.html", message="Elokuvalla pitää olla edes yksi genre")
    description=request.form["description"]
    if description == "":
        return render_template("suggestion_error.html", message="Elokuvalla pitää olla kuvaus")
    leading_roles=request.form["leading_roles"]
    if leading_roles == "":
        return render_template("add_movie_error.html", message="Elokuvalla pitää olla edes yksi päärooli")

    if suggestions.make_suggestion(name, year, genres, description, leading_roles):
        return render_template("new_suggestion.html")
    else:
        return render_template("suggestion_error.html", message="Ehdotuksen lisääminen epäonnistui")

@app.route("/add_movie", methods=["GET","POST"])
def add_movie():
    users.require_admin()
    if request.method == "GET":
        return render_template("add_movie.html")
    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]
        if len(name) < 1 or len(name) > 177:
            return render_template("add_movie_error.html", message="Elokuvan nimi pitää olla 1-177 merkkiä.")
        if movies.check_if_movie_exists(name):
            return render_template("add_movie_error.html", message="Tämän niminen elokuva on jo olemassa.")
        year = request.form["year"]
        if len(year) != 4:
            return render_template("add_movie_error.html", message="Vuosiluvussa pitää olla 4 numeroa")
        if int(year) > 2021:
            return render_template("add_movie_error.html", message="Julkaisu vuosi ei voi olla uudempi kuin 2021")
        genres = request.form["genre"]
        if genres == "":
            return render_template("add_movie_error.html", message="Elokuvalla pitää olla edes yksi genre")
        description = request.form["description"]
        if description == "":
            return render_template("add_movie_error.html", message="Elokuvalla pitää olla kuvaus")
        leading_roles = request.form["leading_roles"]
        if leading_roles == "":
            return render_template("add_movie_error.html", message="Elokuvalla pitää olla edes yksi päärooli")

        if movies.add_movie(name,year,genres, description, leading_roles):
            return redirect ("/")
        else:
            return render_template("add_movie_error.html", message="Elokuvan lisäys epäonnistui")

@app.route("/suggestions")
def suggestion_page():
    users.require_admin()
    suggestion_list = suggestions.get_suggestions()
    number_of_suggestions = suggestions.get_number_of_suggestions()
    return render_template("suggestions.html", suggestions=suggestion_list, number_of_suggestions=number_of_suggestions)
 
@app.route("/accept", methods=["POST"])
def accept():
    users.require_admin()
    users.check_csrf()
    id = request.form["id"]
    if suggestions.suggested_movie_exists(id):
        return render_template("suggestions_issue.html", message="Tämän niminen elokuva on jo olemassa.")
    suggestions.accept(id)
    return redirect ("/suggestions")

@app.route("/decline", methods=["POST"])
def decline():
    users.require_admin()
    users.check_csrf()
    id = request.form["id"]
    suggestions.decline(id)
    return redirect ("/suggestions")

@app.route("/delete_review", methods=["POST"])
def delete_review():
    users.check_csrf()
    id = int(request.form["review_id"])
    movie_id = request.form["movie_id"]
    reviews.delete_review(id)
    return redirect ("/movie_page/" + str(movie_id))

@app.route("/delete_review_admin", methods=["POST"])
def delete_review_admin():
    users.require_admin()
    users.check_csrf()
    id = int(request.form["review_id"])
    movie_id = request.form["movie_id"]
    reviews.delete_review(id)
    return redirect ("/movie_page/" + str(movie_id))

@app.route("/delete_my_review", methods=["POST"])
def delete_my_review():
    users.check_csrf()
    id = request.form["review_id"]
    reviews.delete_review(id)
    return redirect ("/my_reviews")

@app.route("/categories")
def categories_page():
    category_list = categories.get_categories()
    return render_template("categories_page.html", categories=category_list)


@app.route("/category_page/<int:id>")
def category_page(id):
    if not categories.get_category_name(id):
        return render_template("issue.html", message="Valitettavasti kategoriaa ei löydy")
    category_name = categories.get_category_name(id)
    if not categories.get_category_contents(id):
        return render_template("empty_category.html", category_name=category_name, id=id)
    movie_list = categories.get_category_contents(id)
    return render_template("category_page.html", movies=movie_list, category_name=category_name, id=id)

@app.route("/delete_category", methods=["POST"])
def delete_category():
    users.require_admin()
    users.check_csrf()
    category_id = request.form["category_id"]
    categories.delete_category(category_id)
    return redirect ("/categories")

@app.route("/movie_to_category", methods=["POST"])
def movie_to_category():
    users.require_admin()
    users.check_csrf()
    category_id = request.form["category_id"]
    movie_name = request.form["movie_name"]
    if categories.check_movie_in_category(movie_name, category_id):
        return render_template("category_issue.html", message="Elokuva on jo tässä kategoriassa", id=category_id)
    if not movies.check_if_movie_exists(movie_name):
        return render_template("category_issue.html", message="Elokuvaa ei löydy", id=category_id)
    elif categories.movie_to_category(category_id, movie_name):
        return redirect ("/category_page/" + str(category_id))
    else:
        return render_template("category_issue.html", message="Elokuvan lisääminen ei onnistunut", id=category_id)

@app.route("/add_category", methods=["POST"])
def add_category():
    users.require_admin()
    users.check_csrf()
    name = request.form["category_name"]
    categories.add_category(name)
    return redirect ("/categories")

@app.route("/search_results")
def serach_results():
    query = request.args["query"]
    results = movies.search_movie(query)
    return render_template("search_results.html", results=results)

@app.route("/delete_movie", methods=["POST"])
def delete_movie():
    users.require_admin()
    users.check_csrf()
    movie_id = request.form["movie_id"]
    movies.delete_movie(movie_id)
    return redirect("/")

@app.route("/delete_movie_from_category", methods=["POST"])
def delete_movie_from_category():
    users.require_admin()
    users.check_csrf()
    movie_id = request.form["movie_id"]
    category_id = request.form["category_id"]
    if categories.delete_movie_in_category(movie_id, category_id):
        return redirect("/category_page/" + str(category_id))
    else:
        return render_template("category_issue.html", message="Elokuvan poistaminen kategoriasta epäonnistui", id=category_id)

@app.route("/admins")
def admins():
    users.require_admin()
    admins = users.list_admins()
    number_of_admins = users.get_number_of_admins()
    return render_template("admins.html", admins=admins, number_of_admins=number_of_admins)

@app.route("/new_admin", methods=["POST"])
def new_admin():
    users.require_admin
    users.check_csrf()
    username = request.form["username"]
    if len(username) <= 1 or len(username) >= 20:
        return render_template("admins_issue.html", message="Käyttäjätunnuksessa oltava 1-20 merkkiä")
    if not users.username_exists_already(username):
        return render_template("admins_issue.html", message="Käyttäjää ei löydy.")
    if users.check_if_admin(username):
        return render_template("admins_issue.html", message="Kyseinen käyttäjä on jo ylläpitäjä.")
    if users.turn_user_into_admin(username):
        return redirect("/admins")
    else:
        render_template("admins_issue.html", message="Käyttäjän muuttaminen ylläpitäjäksi epäonnistui")

@app.route("/test")
def test():
    return render_template("layout.html")