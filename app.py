from flask import Flask, render_template, request, redirect, url_for, jsonify
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route("/")
def index():
    # Render the login page
    return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Assuming you have form fields named 'username' and 'password' in your signup.html
        username = request.form['username']
        password = request.form['password']
        # Process the signup form
        # Insert the user's data into your database and perform any necessary validation
        # For demonstration purposes, redirect to the home page
        return redirect(url_for('home'))
    # If the request method is GET, render the signup page
    return render_template("signup.html")

@app.route("/home")
def home():
    # Render the home page
    return render_template("home.html")  # Ensure the path is correct, might be just "home.html" without "templates/"

@app.route("/scanitem")
def scanitem():
    # Render the page for scanning items, assuming "cam.html" is the file for capturing images
    return render_template("cam.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form
        username = request.form['username']
        password = request.form['password']
        # Validate the user's credentials with your database
        # If valid, log the user in and redirect to the home page
        return redirect(url_for('home'))
    # If the request method is GET, render the login page
    return render_template("index.html")

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    image_data = data['image']
    image_data = image_data.split(",")[1]  # Remove the header from the base64 encoded string
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    # Save the image or process it
    image.save("captured_image.png")
    # Respond back to the client
    return jsonify({'message': 'Image captured and saved successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
