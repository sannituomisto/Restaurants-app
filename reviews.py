from database import db
from sqlalchemy.sql import text
import datetime
from flask import session

def add_review(restaurant_id, comment):
    username = session["user_name"]
    try:
        sql = text("INSERT INTO review (restaurant_id, username, comment, time) VALUES (:restaurant_id, :username, :comment, NOW())")
        db.session.execute(sql, {"restaurant_id": restaurant_id, "username":username, "comment":comment,  "time":datetime.datetime.now()})
        db.session.commit()
        return True
    except:
        return False
