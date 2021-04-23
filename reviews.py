from db import db

def get_reviews(movie_id):
	sql= "SELECT u.username, r.review, r.grade, r.time FROM reviews r, users u where movie_id=:movie_id and u.id=r.user_id"
	result = db.session.execute(sql, {"movie_id":movie_id})
	reviews = result.fetchall()
	return reviews

def create_review(movie_id, grade, review):
	user_id=session["user_id"]
	sql= "INSERT INTO reviews (user_id, movie_id, grade, review, time) VALUES (:user_id, :movie_id, :grade, :review, Now())"
	db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id, "grade":grade, "review":review})
	db.session.commit()

