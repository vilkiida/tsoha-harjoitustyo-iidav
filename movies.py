from db import db

def get_movie_list():
	sql = "SELECT id, name, year FROM movies ORDER BY year DESC"
	result = db.session.execute(sql)
	movies = result.fetchall()
	return movies

def get_movie_info(id):
	sql="SELECT name, year, genre, description, leading_roles, id FROM Movies WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	information = result.fetchall()
	return information

def add_movie(name,year,genre,description,leading_roles):
       	year=int(year)
        sql="INSERT INTO movies (name,year,genre,description,leading_roles) VALUES (:name,:year,:genre,:description,:leading_roles)"
        db.session.execute(sql, {"name":name, "year":year, "genre":genre, "description":description, "leading_roles":leading_roles})
        db.session.commit()

def search_movie(query):
	sql="SELECT id, name, year, description from movies where name LIKE :query or description LIKE :query"
	result=db.session.execute(sql, {"query":"%"+query+"%"})
	results=result.fetchall()
	if results != None:
		return results
	else:
		return "Haulla ei ollut tuloksia."

def delete_movie(movie_id):
	sql="DELETE FROM movies_in_categories where movie_id=:movie_id"
	db.session.execute(sql, {"movie_id":movie_id})
	sql2="DELETE FROM movies where id=:movie_id"
	db.session.execute(sql2, {"movie_id":movie_id})
	db.session.commit()

