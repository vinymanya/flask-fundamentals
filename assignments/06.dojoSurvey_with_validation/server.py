from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

app.secret_key = "{w[fpwogwjg32264!@#$%^&*(xz)kdfvjflk"
# Index route
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods= ["POST", "GET"])
def result():
	if len(request.form["name"]) < 1:
		flash("Name cannot be empty!")
		return redirect(url_for("index"))
	elif len(request.form["comment"]) > 120:
		flash("Comment cannot be more than 120 characters long!")
		return redirect(url_for("index"))
	elif len(request.form["comment"]) < 1:
		flash("Why don't you leave a short comment and tell us a little bit about yourself???")
		return redirect(url_for("index"))
	# Save user's name in session 
	session["name"] = request.form["name"]
	context = {
		"name" : request.form["name"],
		"location": request.form["location"],
		"fav_lang": request.form["fav_lang"],
		"comment": request.form["comment"]
	}
	return render_template("result.html", context=context)


app.run(debug=True) 