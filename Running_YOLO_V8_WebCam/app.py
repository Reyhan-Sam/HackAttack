from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    # Render log in and sign up
    return render_template("index.html")

@app.route("/signup")
def signup():
    # Render signup page
    return render_template("signup.html")

@app.route("/home")
def home():
    # Render login/signup
    return render_template("home.html")

@app.route("/scanitem")
def scanitem():
    # Render scanning items
    return render_template("scanItem.html")

@app.route("/viewInventory")
def scanitem():
    # Render view inventory
    return render_template("viewInventory.html")

@app.route("/createrecipe")
def scanitem():
    return render_template("createRecipe.html")

if __name__ == "__main__":
    app.run(debug=True)
