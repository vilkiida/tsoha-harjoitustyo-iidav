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

