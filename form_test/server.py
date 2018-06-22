from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# secret key
app.secret_key = "ThisIsSecret"

# Index route
@app.route("/")
def index():
	return render_template("index.html")

# This route will handle our form submission
# Notice how we defined which Http method are allowed by this route
@app.route("/users", methods=["POST"])
def create_user():
	print "Got a post request!"
	# Store the name and email in session by creating name and email keys in session
	session["name"] = request.form["name"]
	session["email"] = request.form["email"]
	return redirect("/show")

# show user's data
@app.route("/show")
def show_user():
	return render_template("user.html", name=session["name"], email=session["email"])

app.run(debug=True) # Run the app in debug mode
