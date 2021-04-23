from db import db

def get_movie_list():
	sql = "SELECT id, name, year FROM movies ORDER BY year DESC"
	result = db.session.execute(sql)
	movies = result.fetchall()
	return movies

def get_movie_info(id):
	sql="SELECT name, year, genre, description, leading_roles FROM Movies WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	information = result.fetchall()
	return information
