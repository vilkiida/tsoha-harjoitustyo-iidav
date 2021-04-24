from db import db

def get_categories():
	sql="SELECT id, name FROM categories"
	result=db.session.execute(sql)
	category_list=result.fetchall()
	return category_list

def get_category_contents(id):
	sql="SELECT m.name, m.year, m.id from movies_in_categories c, movies m where m.id=c.movie_id and c.movie_id=:id"
	result=db.session.execute(sql, {"id":id})
	movie_list=result.fetchall()
	return movie_list

def get_category_name(id):
	sql="SELECT name from categories where id=:id"
	result=db.session.execute(sql, {"id":id})
	category_name=result.fetchone()[0]
	return category_name

