from db import db

def get_categories():
	sql="SELECT id, name FROM categories ORDER BY name"
	result=db.session.execute(sql)
	category_list=result.fetchall()
	return category_list

def get_category_contents(id):
	sql="SELECT m.name, m.year, m.id from movies_in_categories c, movies m where m.id=c.movie_id and c.category_id=:id"
	result=db.session.execute(sql, {"id":id})
	movie_list=result.fetchall()
	if movie_list == []:
		return False
	return movie_list

def get_category_name(id):
	try:
		sql="SELECT name from categories where id=:id"
		result=db.session.execute(sql, {"id":id})
		category_name=result.fetchone()[0]
	except:
		return False
	return category_name

def delete_category(id):
	sql="DELETE FROM movies_in_categories where category_id=:id"
	db.session.execute(sql, {"id":id})
	sql2="DELETE FROM categories where id=:id"
	db.session.execute(sql2, {"id":id})
	db.session.commit()

def movie_to_category(id, movie_name):
	sql="SELECT id from movies where name=:movie_name"
	result=db.session.execute(sql, {"movie_name":movie_name})
	movie_id=result.fetchone()
	if movie_id == None:
		return False
	movie_id=movie_id[0]
	try:
		sql2="INSERT INTO movies_in_categories VALUES (:id,:movie_id)"
		db.session.execute(sql2, {"id":id, "movie_id":movie_id})
		db.session.commit()
	except:
		return False
	return True

def add_category(name):
	sql="INSERT INTO categories (name) VALUES (:name)"
	db.session.execute(sql, {"name":name})
	db.session.commit()

def check_movie_in_category(moviename, category_id):
	sql="SELECT c.category_id from movies_in_categories c, movies m where m.id=c.movie_id and m.name=:moviename"
	result=db.session.execute(sql, {"moviename":moviename})
	id_s=result.fetchall()
	if id_s != None:
		for id in id_s:
			if int(id[0]) == int(category_id):
				return True
	else:
		return False

def delete_movie_in_category(movie_id, category_id):
	try:
		sql="DELETE from movies_in_categories where movie_id=:movie_id and category_id=:category_id"
		db.session.execute(sql, {"movie_id":movie_id, "category_id":category_id})
		db.session.commit()
	except:
		return False
	return True