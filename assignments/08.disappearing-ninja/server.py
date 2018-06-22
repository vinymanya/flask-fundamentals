from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

# route handle to display all ninjas
@app.route("/ninja")
def ninjas():
	all_ninjas = []
	images = os.listdir("./static/images")
	for ninja_image in images:
		if ninja_image.endswith(".jpg") and ninja_image != "notapril.jpg":
			all_ninjas.append(os.path.join("./static/images", ninja_image))
		else:
			continue
	print all_ninjas
	return render_template("ninja.html", all_ninjas= all_ninjas, image_alt= "Turtle Ninja Image")

# Route handler displaying only one ninja image
@app.route("/ninja/<color>")
def one_ninja_image(color):
	if color == "blue":
		turtle = "leonardo"
	elif color == "purple":
		turtle = "donatello"
	elif color == "red":
		turtle = "raphael"
	elif color == "orange":
		turtle = "michelangelo"
	else:
		turtle = "notapril"
	print turtle
	return render_template("ninja_color.html", turtle=turtle, alt = turtle)

app.run(debug=True)