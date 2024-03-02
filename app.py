from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    # Render log in and sign up
    return render_template("index.html")

@app.route("/signup")
def signup():
    # Render  signup page
    return render_template("signup.html")

@app.route("/home")
def home():
    # Render home page after login/signup
    return render_template("home.html")

@app.route("/scanitem")
def scanitem():
    # Render the page for scanning items
    return render_template("scanitem.html")

if __name__ == "__main__":
    app.run(debug=True)




