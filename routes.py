from app import app
import users
import restaurants
import reviews
import favorites
from flask import render_template, request, redirect

@app.route("/")
def index():
    return redirect("/home_page")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/home_page")
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

        return redirect("/home_page")


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

        return redirect("/home_page")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/home_page", methods=["GET", "POST"])
def home_page():
    if request.method == "GET":
        if users.is_user():
            return render_template("home_page.html", restaurants_info=restaurants.get_short_info(), favorites=favorites.get_favorites())
        else:
            return render_template("home_page.html", restaurants_info=restaurants.get_short_info())
        
    if request.method == "POST":
        sort_value=request.form["sort"]
        return redirect("/sorted_list/"+sort_value)
    
@app.route("/sorted_list/<sort_value>")
def sorted_list(sort_value):
        return render_template("sortedrestaurants.html", sortedrestaurants=restaurants.get_short_info(sort_value), sort_value=sort_value)
    

@app.route("/new_restaurant", methods=["GET", "POST"])
def new_restaurant():
    if request.method == "GET":
        if users.is_admin:
            return render_template("new_restaurant.html")
        else:
            return render_template("error.html", message= "Only admins can add a new restaurant")


    if request.method == "POST":
        users.check_csrf()
        if users.is_admin:
            name = request.form["name"]
            address = request.form["address"]
            price_range = request.form["price_range"]
            category = request.form["category"]
            description = request.form["description"]
            opening_hours={1:[request.form["open_1"], request.form["close_1"], request.form["status_1"]], 2:[request.form["open_2"], request.form["close_2"], request.form["status_2"]], 3:[request.form["open_3"],
            request.form["close_3"], request.form["status_3"]], 4:[request.form["open_4"], request.form["close_4"], request.form["status_4"]], 5:[request.form["open_5"], request.form["close_5"], request.form["status_5"]], 6:[request.form["open_6"],
            request.form["close_6"], request.form["status_6"]], 7:[request.form["open_7"], request.form["close_7"], request.form["status_7"]]}

            if len(name) > 40 or len(name) < 1:
                return render_template("error.html", message="Invalid name")

            if len(address) > 40 or len(address) < 1:
                return render_template("error.html", message="Invalid address")
            
            if price_range == "none":
                return render_template("error.html", message="Please select price range")
            
            if category == "none":
                return render_template("error.html", message="Please select category")

            if len(description) > 200 or len(description) < 1:
                return render_template("error.html", message="Invalid description")

            if not restaurants.new_restaurant(name, address, price_range, category, description):
                return render_template("error.html", message="Submit failed. There is already restaurant with this address.")

            for day in opening_hours:
                if not restaurants.add_opening_hours(restaurants.restaurant_id(address), day, opening_hours[day][0], opening_hours[day][1], opening_hours[day][2]):
                    return render_template("error.html", message="Submit failed. Check opening hours.")

            return redirect("/home_page")

        else:
            return render_template("error.html", message= "Only admins can add a new restaurant")

@app.route("/restaurant/<int:restaurant_id>", methods=["GET"])
def show_info(restaurant_id):
    if request.method == "GET":
        info = restaurants.get_full_info(restaurant_id)
        o_hours=restaurants.get_opening_hours(restaurant_id)
        if users.is_user():
            get_user=users.get_user()
            restaurant_reviews=reviews.get_reviews(restaurant_id)
            average_rating=reviews.get_average_rating(restaurant_id)
            is_favorite=favorites.check_if_in_favorites_already(restaurant_id)
            return render_template("restaurant.html", user=get_user, restaurant_id=restaurant_id, name=info[0], address=info[1], price_range=info[2], category=info[3],
                description=info[4], opening_hours=o_hours, reviews=restaurant_reviews, favorite=is_favorite, average_rating=average_rating)
        else:
            return render_template("restaurant.html", restaurant_id=restaurant_id, name=info[0], address=info[1], price_range=info[2], category=info[3],
                description=info[4], opening_hours=o_hours)



@app.route("/review/<int:restaurant_id>", methods=["GET", "POST"])
def review(restaurant_id):
    if request.method == "GET":
        info=restaurants.get_full_info(restaurant_id)
        if users.is_user():
            return render_template("review.html", restaurant_id = restaurant_id, name=info[0])
        else:
            return render_template("error.html", message= "You can not give a review if you are not signed in")

    if request.method == "POST":
        users.check_csrf()
        if users.is_user():
            comment = request.form["comment"]
            rating= request.form["rating"]

            if rating == "none":
                return render_template("error.html", message="Please select rating")
            
            if len(comment) > 400:
                return render_template("error.html", message="Comment too long")
            
            reviews.add_review(restaurant_id, comment, rating)

            return redirect("/restaurant/"+str(restaurant_id))
        
        else:
            return render_template("error.html", message= "You can not give a review if you are not signed in")

@app.route("/add_favorite", methods=["POST"])
def add_favorite():
    if request.method == "POST":
        users.check_csrf()
        if users.is_user:
            restaurant_id = request.form["restaurant_id"]
            if favorites.check_if_in_favorites_already(restaurant_id):
                favorites.add_to_favorites(restaurant_id)
                return redirect("/restaurant/"+str(restaurant_id))
            else:
                return render_template("error.html", message= "Already in favorites")
        else:
            return render_template("error.html", message= "You can not add favorites if you are not signed in")

@app.route("/remove_restaurant", methods=["POST"])
def remove_restaurant():
    if request.method == "POST":
        users.check_csrf()
        if users.is_admin:
            restaurant_id = request.form["restaurant_id"]
            restaurants.remove_restaurant(restaurant_id)
            return redirect("/home_page")
    
@app.route("/remove_review", methods=["POST"])
def remove_review():
    if request.method == "POST":
        users.check_csrf()
        if users.is_user:
            review_id = request.form["review_id"]
            restaurant_id = request.form["restaurant_id"]
            reviews.remove_review(review_id)
            return redirect("/restaurant/"+str(restaurant_id))
        
@app.route("/remove_favorite", methods=["POST"])
def remove_favorite():
    if request.method == "POST":
        users.check_csrf()
        if users.is_user:
            restaurant_id = request.form["restaurant_id"]
            favorites.remove_from_favorites(restaurant_id)
            return redirect("/restaurant/"+str(restaurant_id))
        
@app.route("/remove_user", methods=["POST"])
def remove_user():
    if request.method == "POST":
        users.check_csrf()
        if users.is_user:
            username=users.get_user()
            users.delete_user(username)
            return redirect("/home_page")




