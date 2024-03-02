from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!" 
def home2():
    return "yo boii"
