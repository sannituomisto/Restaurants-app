from database import db
from sqlalchemy.sql import text
from flask import session

def add_to_favorites(restaurant_id):
    #try:
        username = session["user_name"]
        sql = text("""INSERT INTO favorites (username, restaurant_id) VALUES (:username, :restaurant_id)""")
        db.session.execute(sql, {"username":username, "restaurant_id":restaurant_id})
        db.session.commit()
        #return True
    #except:
        #return False

def check_if_in_favorites_already(restaurant_id):
    username = session["user_name"]
    sql = text("SELECT restaurant_id FROM favorites WHERE username = :username")
    result = db.session.execute(sql, {"username":username})
    favorite_restaurants=result.fetchall()
    favorites=[]
    for restaurant in favorite_restaurants:
        favorites.append(restaurant[0])
    if restaurant_id in favorites:
        return False
    return True

def get_favorites():
    username = session["user_name"]
    sql = text("SELECT restaurant_id FROM favorites WHERE username = :username")
    result = db.session.execute(sql, {"username":username})
    favorite_restaurants=result.fetchall()
    favorites=[]
    for restaurant_id in favorite_restaurants:
        sql = text("SELECT id, name, address FROM restaurants WHERE id = :restaurant_id")
        result2 = db.session.execute(sql, {"restaurant_id":restaurant_id[0]}).fetchone()
        favorites.append(result2)
    return favorites

def remove_from_favorites(restaurant_id):
    username = session["user_name"]
    sql = text("DELETE FROM favorites WHERE restaurant_id = :restaurant_id and username = :username")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "username":username})
    db.session.commit()

