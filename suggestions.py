from db import db
from flask import session

def make_suggestion(name, year, genre, description, leading_roles):
	try:
		year = int(year)
		user_id = session["user_id"]
		sql = """INSERT INTO suggestions (name, year, genre, description, 
		leading_roles, user_id, time,accepted) VALUES (:name, :year, :genre, 
		:description, :leading_roles, :user_id, NOW(),0)"""
		db.session.execute(sql, {"name":name, "year":year, "genre":genre, "description":description, "leading_roles":leading_roles, "user_id":user_id})
		db.session.commit()
	except:
		return False
	return True

def get_suggestions():
	sql = """SELECT s.name, s.year, s.genre, s.description, s.leading_roles, 
	u.username, s.time, s.id from suggestions s, users u where s.user_id=u.id 
	and accepted=0 order by s.time"""
	result = db.session.execute(sql)
	suggestions = result.fetchall()
	return suggestions

def get_number_of_suggestions():
	sql = "Select count(*) from suggestions where accepted=0"
	result = db.session.execute(sql)
	number_of_suggestions = result.fetchone()[0]
	if number_of_suggestions != None:
		return number_of_suggestions
	else:
		return 0

def accept(id):
	sql = "Update suggestions SET accepted=1 WHERE id=:id"
	db.session.execute(sql, {"id":id})
	suggestion_to_a_movie(id)

def suggestion_to_a_movie(id):
	sql = "SELECT name, year, genre, description, leading_roles from suggestions where id=:id"
	result = db.session.execute(sql, {"id":id})
	info = result.fetchall()[0]
	name = info[0]
	year = info[1]
	genre = info[2]
	description = info[3]
	leading_roles = info[4]
	sql2 = """INSERT INTO movies (name, year, genre, description, 
	leading_roles) VALUES (:name, :year, :genre, :description, :leading_roles)"""
	db.session.execute(sql2, {"name":name, "year":year, "genre":genre, "description":description, "leading_roles":leading_roles})
	db.session.commit()

def decline(id):
	sql = "Update suggestions SET accepted=2 WHERE id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()

def suggested_movie_exists(id):
	sql = "Select m.name from movies m, suggestions s where s.name=m.name and s.id=:id" 
	result = db.session.execute(sql, {"id":id})
	moviename = result.fetchone()
	if moviename == None:
		return False
	else:
		return True