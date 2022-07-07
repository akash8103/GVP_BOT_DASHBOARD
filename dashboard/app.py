from flask import Flask, render_template, session, redirect, Response
from functools import wraps
import json
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.Chatbot

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('index.html')

#Tables Page
@app.route('/tables', methods=["GET"])
def tables():
    return render_template("tables.html")

#Charts Page
@app.route('/charts', methods=["GET"])
def charts():
    return render_template("charts.html")

#profile Page
@app.route('/profile', methods=["GET"])
def profile():
    return render_template("profile.html")
