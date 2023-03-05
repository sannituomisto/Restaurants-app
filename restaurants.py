from sqlalchemy.sql import text
from database import db

def new_restaurant(name, address, price_range, category, description):
    try:
        sql = text("""INSERT INTO restaurants (name, address, price_range, category, description) VALUES (:name, :address, :price_range, :category, :description)""")
        db.session.execute(sql, {"name":name, "address":address, "price_range":price_range, "category":category, "description":description})
        db.session.commit()
        return True
    except:
        return False

def add_opening_hours(restaurant_id, day, open, close, status):
    try:
        sql = text("""INSERT INTO opening_hours (restaurant_id, day, open, close, status) VALUES (:restaurant_id, :day, :open, :close, :status)""")
        db.session.execute(sql, {"restaurant_id":restaurant_id, "day":day, "open":open, "close":close, "status":status})
        db.session.commit()
        return True
    except:
        return False

def get_short_info(sort="name"):
    if sort == "name":
        sql = text("SELECT id, name, address FROM restaurants ORDER BY name")
    if sort == "lowest_price":
        sql = text("SELECT id, name, address FROM restaurants ORDER BY price_range")
    if sort == "highest_price":
        sql = text("SELECT id, name, address FROM restaurants ORDER BY price_range DESC")
    if sort == "rating":
        sql = text("SELECT res.id, res.name, res.address FROM restaurants AS res LEFT JOIN (SELECT restaurant_id, AVG(rating) AS rest_rat FROM review GROUP BY restaurant_id) AS rat_ave ON res.id = rat_ave.restaurant_id ORDER BY COALESCE(rat_ave.rest_rat,0) DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def get_full_info(restaurant_id):
    sql = text("SELECT name, address, price_range, category, description FROM restaurants WHERE id=:restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchone()

def get_opening_hours(restaurant_id):
    sql = text("SELECT day, open, close, status FROM opening_hours WHERE restaurant_id=:restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()


def restaurant_id(address):
    sql=text("SELECT id FROM restaurants WHERE address=:address")
    result = db.session.execute(sql, {"address":address})
    return result.fetchone()[0]

def remove_restaurant(restaurant_id):
    sql=text("DELETE FROM restaurants WHERE id=:restaurant_id")
    db.session.execute(sql, {"restaurant_id":restaurant_id})
    db.session.commit()
