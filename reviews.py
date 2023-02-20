from database import db
from sqlalchemy.sql import text
import datetime
from flask import session

def add_review(restaurant_id, comment, rating):
    username = session["user_name"]
    if len(comment) >= 1:
        sql = text("INSERT INTO review (restaurant_id, username, comment, rating, time) VALUES (:restaurant_id, :username, :comment, :rating, NOW())")
        db.session.execute(sql, {"restaurant_id": restaurant_id, "username":username, "comment":comment, "rating":rating, "time":datetime.datetime.now()})
        db.session.commit()
    else:
        sql = text("INSERT INTO review (restaurant_id, username, rating, time) VALUES (:restaurant_id, :username, :rating, NOW())")
        db.session.execute(sql, {"restaurant_id": restaurant_id, "username":username, "rating":rating, "time":datetime.datetime.now()})
        db.session.commit()


