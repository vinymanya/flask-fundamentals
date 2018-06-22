from flask import Flask, render_template

app = Flask(__name__)

# Index route
@app.route("/")
def index():
	return render_template("index.html")

# ninjas route
@app.route("/ninjas")
def ninjas():
	return render_template("ninjas.html")

# Dojos route
@app.route("/dojos/new")
def dojos():
	return render_template("dojos.html")


app.run(debug=True) # Run the app in debug mode