from db import db
from flask import session
def get_reviews(movie_id):
	sql = "SELECT u.username, r.review, r.grade, r.time, r.id, u.id FROM reviews r, users u where movie_id=:movie_id and u.id=r.user_id"
	result = db.session.execute(sql, {"movie_id":movie_id})
	reviews = result.fetchall()
	return reviews

def create_review(movie_id, grade, review):
	try:
		user_id = session["user_id"]
		sql = "INSERT INTO reviews (user_id, movie_id, grade, review, time) VALUES (:user_id, :movie_id, :grade, :review, Now())"
		db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id, "grade":grade, "review":review})
		db.session.commit()
	except:
		return False
	return True

def get_amount(movie_id):
	sql = "SELECT count(*) from reviews where movie_id=:movie_id"
	result = db.session.execute(sql,{"movie_id":movie_id})
	review_amount = result.fetchone()[0]
	if review_amount != None:
		return review_amount
	else:
		return 0

def get_average(movie_id):
	sql = "Select AVG(grade) from reviews where movie_id=:movie_id"
	result = db.session.execute(sql,{"movie_id":movie_id})
	average = result.fetchone()[0]
	if average != None:
		average=f"{average:.1f}"
		return average
	else:
		return "-"

def get_my_reviews():
	user_id = session["user_id"]
	sql = "Select m.name, r.review, r.grade, r.time, r.id from reviews r, movies m where r.user_id=:user_id and m.id=r.movie_id"
	result = db.session.execute(sql, {"user_id":user_id})
	my_reviews = result.fetchall()
	return my_reviews

def get_number_of_reviews():
	user_id = session["user_id"]
	sql = "Select count(*) from reviews where user_id=:user_id"
	result = db.session.execute(sql, {"user_id":user_id})
	number_of_reviews = result.fetchone()[0]
	if number_of_reviews != None:
		return number_of_reviews
	else:
		return 0

def delete_review(id):
	sql = "DELETE FROM reviews WHERE id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()

