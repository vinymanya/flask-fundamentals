from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Create a session key
app.secret_key = 'F12Zr47jyX R~X@H!jmM]Lwf/,?KTW%'

# index route
@app.route("/")
def index():
	# First time visitor
	if "counter" not in session:
		session["counter"] = 1
	# If counter exists in session
	else:
		session["counter"] += 1
	return render_template("index.html")

# Ninjas challenge
# create a +2 button that increments counter by 2 and reloads the page
@app.route("/add")
def add_counter():
	# Increment counter by 2
	session["counter"] += 2
	return redirect("/")


# hacker challenge
# add a reset button that will reset the counter to 1
@app.route("/reset")
def reset_counter():
	# Clear session
	session.clear()
	return redirect("/")

app.run(debug=True)


