from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
import random

app = Flask(__name__)

app.secret_key = "3984794!@#$%^&*()euritoombvn"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Index route
@app.route("/")
def index():
	if "users" not in session:
		session["users"] = []
		session["counter"] = 0
	return render_template("index.html")

# create users route
@app.route("/user", methods=["POST"])
def create_user():
	if len(request.form["first_name"]) < 1:
		flash("First Name cannot be empty!", "error")
	elif len(request.form["last_name"]) < 1:
		flash("Last Name cannot be empty!", "error")
	elif not EMAIL_REGEX.match(request.form["email"]):
		flash("Invalid Email Address!", "error")
	else:
		user = {
			"first_name": request.form["first_name"],
			"last_name": request.form["last_name"],
			"email": request.form["email"],
			"id": random.randint(1, 100)
		}
		session["counter"] += int(request.form["count"])
		session["users"].append(user)
		flash("You have been successfully registered!", "success")
		return redirect("/")
	return redirect(url_for("index"))

# Dynamic Advanced routing
@app.route("/user/<id>")
def show_user(id):
	# Get the user with that id
	for user in session["users"]:
		if user["id"] == id:
			one_user = user
		# else:
		# 	one_user = "Nothing"
		# 	return render_template("user.html", user=one_user)
	return render_template("user.html", user=one_user)		


# clear session
@app.route("/clear")
def erase_session():
	session.clear()
	return redirect(url_for("index"))

app.run(debug=True)
