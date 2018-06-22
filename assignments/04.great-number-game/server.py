from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "sjkfeh(9)0ij5&*2#z$%!@wsbfsalkj4#DF^"

@app.route("/")
def index():
	# Check if 'target' exist in session
	if "target" not in session:
		# Generate a random number and store it in session
		session["target"] = random.randrange(0, 101)
	return render_template("index.html")

# Create a route that process the form submission
@app.route("/process", methods=["POST"])
def process_form():
	# You can't compare a string with an integer therefore use int() method to convert a str to an int
	if int(request.form["guess"]) == session["target"]:
		session["result"] = "Correct"
	elif int(request.form["guess"]) > session["target"]:
		session["result"] = "high"
	elif int(request.form["guess"]) < session["target"]:
		session["result"] = "low"
	return redirect("/")

# Make the user replay the game after winning
@app.route("/replay")
def play_again():
	session.clear()
	# OR
	# session.pop("target")
	# session.pop("result")
	return redirect("/")


# Run the app in debug mode
app.run(debug=True)