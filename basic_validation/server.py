from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

app.secret_key = "1-2946-1-02ofhiejk#$%&*(!@"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_form():
	# do some validations here!
	if len(request.form["name"]) < 1:
		# display an error message
		flash("Name cannot be empty!")
	else:
		# display success message
		flash("Success! Your name is {}".format(request.form["name"]))
	return redirect(url_for("index")) # Import url_for method to start using in all of your redirects.

app.run(debug=True)