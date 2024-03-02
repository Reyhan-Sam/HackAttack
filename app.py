import torch    
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, rendor_template
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"  
