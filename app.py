from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/cam")
def cam():
    return render_template("cam.html")



