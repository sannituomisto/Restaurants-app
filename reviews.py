from database import db
from sqlalchemy.sql import text
import datetime
from flask import session

def add_review(restaurant_id, comment, rating):
    username = session["user_name"]
    if len(comment) >= 1:
        sql = text("INSERT INTO review (restaurant_id, username, comment, rating) VALUES (:restaurant_id, :username, :comment, :rating)")
        db.session.execute(sql, {"restaurant_id": restaurant_id, "username":username, "comment":comment, "rating":rating})
        db.session.commit()
    else:
        sql = text("INSERT INTO review (restaurant_id, username, rating) VALUES (:restaurant_id, :username, :rating)")
        db.session.execute(sql, {"restaurant_id": restaurant_id, "username":username, "rating":rating})
        db.session.commit()

def get_reviews(restaurant_id):
    sql = text("SELECT id, username, comment, rating, time FROM review WHERE restaurant_id = :restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()

def remove_review(review_id):
    sql = text("DELETE FROM review WHERE id = :review_id")
    db.session.execute(sql, {"review_id":review_id})
    db.session.commit()

def get_average_rating(restaurant_id):
    sql = text("SELECT AVG(rating), COUNT(rating) FROM review WHERE restaurant_id = :restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id}).fetchone()
    count=result[1]
    average=result[0]
    if count > 0:
        return (("%.2f" % average, count))
    else:
        return ((average, count))





