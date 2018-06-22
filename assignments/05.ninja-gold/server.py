from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "364r9rWR639GYHY13Hrjyh@#$^&*(@w)_89"

@app.route("/")
def index():
	if "activities" not in session:
		session["activities"] = []
	if "gold" not in session:
		session["gold"] = 0
	return render_template("index.html")

# process_money route
@app.route("/process_money", methods=["POST"])
def process_money():
	if request.form["building"] == "farm":
		gold = random.randint(10, 20)
		session["gold"] += gold
		activity = "Earned " + str(gold) + " golds" + " from the farm"
		session["activities"].append(activity)
		return redirect("/")

	elif request.form["building"] == "cave":
		gold = random.randint(5, 10)
		session["gold"] += gold
		activity = "Earned " + str(gold) + " golds" + " from the cave"
		session["activities"].append(activity)
		return redirect("/")
	
	elif request.form["building"] == "house":
		gold = random.randint(2, 5)
		session["gold"] += gold
		activity = "Earned " + str(gold) + " golds" +" from the house"
		session["activities"].append(activity)
		return redirect("/")
	
	elif request.form["building"] == "casino":
		gold = random.randint(0, 50)
		session["gold"] += gold
		activity = "Earned " + str(gold) + " golds" + " from the casino"
		session["activities"].append(activity)
		return redirect("/")
		
	return redirect("/")

# create a route for resetting everything
@app.route("/reset")
def reset():
	session.pop("activities")
	session.pop("gold")
	return redirect("/")


# Run the app in debug mode
app.run(debug=True)

