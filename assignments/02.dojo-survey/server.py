from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Index route
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods= ["POST", "GET"])
def result():
	# Process form data here
	context = {
		"name" : request.form["name"],
		"location": request.form["location"],
		"fav_lang": request.form["fav_lang"],
		"comment": request.form["comment"]
	}
	return render_template("result.html", context=context)


app.run(debug=True) 