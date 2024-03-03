from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
import io

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
    # Render home page after login/signup
    return render_template("templates\home.html")

@app.route("/scanitem")
def scanitem():
    # Render the page for scanning items
    # Assume "cam.html" is the file for capturing images
    return render_template("cam.html")

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    image_data = data['image']
    # Remove the header from the base64 encoded string
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    # Save the image or process it
    image.save("captured_image.png")
    # Respond back to the client
    return jsonify({'message': 'Image captured and saved successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
