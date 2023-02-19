from database import db
from sqlalchemy.sql import text

def new_restaurant(name, address, price_range, category, description):
    try:
        sql = text("""INSERT INTO restaurants (name, address, price_range, category, description) VALUES (:name, :address, :price_range, :category, :description)""")
        db.session.execute(sql, {"name":name, "address":address, "price_range":price_range, "category":category, "description":description})
        db.session.commit()
        return True
    except:
        return False

def add_opening_hours(restaurant_id, day, open, close):
    try:
        sql = text("""INSERT INTO opening_hours (restaurant_id, day, open, close) VALUES (:restaurant_id, :day, :open, :close)""")
        db.session.execute(sql, {"restaurant_id":restaurant_id, "day":day, "open":open, "close":close})
        db.session.commit()
        return True
    except:
        return False

def get_short_info():
    sql = text("SELECT id, name, address FROM restaurants")
    result = db.session.execute(sql)
    return result.fetchall()


def get_full_info(restaurant_id):
    sql = text("SELECT name, address, price_range, category, description FROM restaurants WHERE id=:restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchone()

def get_opening_hours(restaurant_id):
    sql = text("SELECT day, open, close FROM opening_hours WHERE restaurant_id=:restaurant_id")
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()


def restaurant_id(name):
    sql=text("SELECT id FROM restaurants WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    return result.fetchone()[0]