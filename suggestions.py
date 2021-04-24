from db import db
from flask import session

def make_suggestion(name, year, genre, description, leading_roles):
	year=int(year)
	user_id=session["user_id"]
	sql="INSERT INTO suggestions (name,year,genre,description,leading_roles, user_id, time) VALUES (:name, :year, :genre, :description, :leading_roles, :user_id, NOW())"
	db.session.execute(sql, {"name":name, "year":year, "genre":genre, "description":description, "leading_roles":leading_roles, "user_id":user_id})
	db.session.commit()
