from database import db
from sqlalchemy.sql import text

def new_restaurant(name, address, price_range, category):
    try:
        sql = text("""INSERT INTO restaurants (name, address, price_range, category) VALUES (:name, :address, :price_range, :category)""")
        db.session.execute(sql, {"name":name, "address":address, "price_range":price_range, "category":category})
        db.session.commit()
        return True
    except:
        return False

    