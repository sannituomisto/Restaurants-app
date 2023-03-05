import os
from database import db
from flask import session, abort, request
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = text("SELECT id, password, is_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if not check_password_hash(hash_value, password):
            return False
        session["user_id"] = user[1]
        session["user_name"] = username
        session["is_admin"] = user[2]
        session["csrf_token"] = os.urandom(16).hex()
        return True

def register(username,password,is_admin):
    hash_value = generate_password_hash(password)
    try:
        sql = text("""INSERT INTO users (username, password, is_admin) VALUES (:username, :password, :is_admin)""")
        db.session.execute(sql, {"username":username, "password":hash_value, "is_admin":is_admin})
        db.session.commit()
    except:
        return False

    return login(username, password)

def delete_user(username):
    try:
        sql = text("DELETE FROM users WHERE username=:username")
        db.session.execute(sql, {"username":username})
        db.session.commit()
    except:
        return False
    
    return logout()


def is_admin():
    try:
        username=session["user_name"]
        sql=text("SELECT is_admin FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username":username})
        is_admin = result.fetchone()
        return is_admin
    except:
        return False

def is_user():
    try:
        if session["user_name"]:
            return True
    except:
        return False
    
def get_user():
    try:
        if session["user_name"]:
            return session["user_name"]
    except:
        return False

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["is_admin"]

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)


    

    

