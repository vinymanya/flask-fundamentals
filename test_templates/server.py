from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", phase="Hello", times=5)


app.run(debug=True) # Run the app in debug mode