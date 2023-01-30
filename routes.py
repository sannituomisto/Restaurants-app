from app import app
import users
from flask import render_template, request, redirect

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            user = users.get_user(username)
            if user.is_admin:
                return redirect("/admin_page")
            else:
                return redirect("/user_page")
        else:
            return render_template("error.html", message = "Wrong username or password")

@app.route("/register_normal_user", methods=["GET", "POST"])
def register_normal_user():
    if request.method == "GET":
        return render_template("register_normal_user.html")

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if len(username) < 1 or len(username) > 15:
            return render_template("error.html", message="Username must have 1-15 characters")

        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")

        if len(password1) < 4:
            return render_template("error.html", message="Password must be at least 4 characters")

        if any(char.isdigit() for char in password1) == False:
            return render_template("error.html", message="Password must contain numbers")

        if not users.register(username, password1, False):
            return render_template("error.html", message="Registration failed")

        return redirect("/normal_user_page")


@app.route("/register_admin", methods=["GET", "POST"])
def register_admin():
    if request.method == "GET":
        return render_template("register_admin.html")

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if len(username) < 1 or len(username) > 15:
            return render_template("error.html", message="Username must have 1-15 characters")

        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")

        if len(password1) < 4:
            return render_template("error.html", message="Password must be at least 4 characters")

        if any(char.isdigit() for char in password1) == False:
            return render_template("error.html", message="Password must contain numbers")

        if not users.register(username, password1, True):
            return render_template("error.html", message="Registration failed")

        return redirect("/admin_page")


@app.route("/admin_page", methods=["GET", "POST"])
def admin_page():
    return render_template("admin_page.html")
    
@app.route("/normal_user_page", methods=["GET", "POST"])
def normal_user_page():
    return render_template("normal_user_page.html")




