from flask import Flask, render_template

app = Flask(__name__)

# Create a route decorator
@app.route("/")
def hello_world():
	return render_template("index.html", name= "Viny")

@app.route("/success")
def success():
	return render_template("success.html")


app.run(debug=True)



