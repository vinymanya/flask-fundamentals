from flask import Flask, render_template, request, redirect, session, url_for, flash
import re
import time # import 'time' module to use time functionalities

app = Flask(__name__)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app.secret_key = "2878#$%^&*()_+!@#eiioi"

pattern = re.compile(r'^\d.*[A-Z]|[A-Z].*\d')

@app.route("/")
def index():
	return render_template("index.html")

# Route to process form data
@app.route("/process", methods=["POST"])
def process_form():
	if len(request.form["firstName"]) < 1 and not request.form["firstName"].isalpha():
		flash("First Name is required and must contain letters only!", "error")
	elif len(request.form["lastName"]) < 1 and not request.form["lastName"].isalpha():
		flash("Last Name is required and must contain letters only!", "error")
	elif len(request.form["email"]) < 1:
		flash("Email is required!", "error")
	elif not EMAIL_REGEX.match(request.form["email"]):
		flash("Invalid Email Address!", "error")
	elif len(request.form["password"]) < 1 or len(request.form["confirm_password"]) < 1:
		flash("Please Enter your password!", "error")
	elif len(request.form["password"]) < 6:
		flash("Password should not be less than 6 characters long!", "error")
	elif request.form["password"] != request.form["confirm_password"]:
		flash("Passwords don't match!", "error")
	# Ninja Challenge:
	# Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value
	elif not pattern.match(request.form["password"]):
		flash("Password must contain at least 1 uppercase letter and 1 numeric value.", "error")			
	# Hacker Challenge:
	# Add a birth-date field that must be validated as a valid date (and must be from the past).
	# if not (time.strptime(request.form["birthDay"], "%Y-%m-%d")):
	# 	flash("Only for those who were born in year 2000!!!", "error" )
	else:
		session["firstName"] = request.form["firstName"]
		flash("You have successfully Registered!", "success")
		return redirect(url_for("success"))
	return redirect(url_for("index"))

@app.route("/success")
def success():
	return render_template("success.html")

# Logout route
@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))

app.run(debug=True)