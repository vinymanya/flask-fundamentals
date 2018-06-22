# Import Flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
# the "re" module will let us perform some regular expression operations
import re

app = Flask(__name__)

app.secret_key = "2747489@#$%&fHGSDFFGRTASDFffg493"
# Create a regular expression object that we can use to run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_form():
	if len(request.form["email"]) < 1:
		flash("Email cannot be blank!")
	# Check if the email doesn't match regular expression
	elif not EMAIL_REGEX.match(request.form["email"]):
		flash("Invalid Email address!")
	else:
		flash("Success")
		print "Your email is: {}".format(request.form["email"])
	return redirect(url_for("index"))

app.run(debug=True)

