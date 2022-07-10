from flask import Flask, render_template, session, redirect, Response
from functools import wraps
from json import dumps
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
  try:
    tusers = db.gvpbot.count_documents({})
    male = db.gvpbot.count_documents({"Gender":"MALE"})
    female = db.gvpbot.count_documents({"Gender":"FEMALE"})
    # english = db.gvpbot.sum({"$English_Language"})
    english = db.gvpbot.count_documents({"English_Language":1})  
    hindi = db.gvpbot.count_documents({"Hindi_Language":1})
    gujarati = db.gvpbot.count_documents({"Gujarati_Language":1})
    return render_template('index.html', tusers=tusers, male=male, female=female, english=english, hindi=hindi, gujarati=gujarati)
    #return dumps(names)
  except Exception as e:
    return dumps({'error' : str(e)})
  # return render_template('index.html')

#Tables Page
@app.route('/tables', methods=["GET"])
def tables():
  try:
    botusers = []

    tbl="<thead><tr><th>Name</th><th>Email ID</th><th>Gender</th><th>Address</th><th>Contact No</th></tr></thead>"
    botusers.append(tbl)

    for y in db.gvpbot.find():
      fname = "%s"%y['fName']
      botusers.append(fname)
      lname = "%s"%y['lName']
      botusers.append(lname)
      # email = "<td>%s</td>"%y['Email_ID']
      # botusers.append(email)
      gender = "%s"%y['Gender']
      botusers.append(gender)
      address = "%s"%y["Address"]
      botusers.append(address)
      # mobile = "%s"%y['Mobile_No']
      # botusers.append(mobile)
    return render_template("tables.html", fname=fname, lname=lname, gender=gender, address=address)
  except Exception as e:
    return dumps({'error' : str(e)})

#Charts Page
@app.route('/charts', methods=["GET"])
def charts():
    return render_template("charts.html")

#profile Page
@app.route('/profile', methods=["GET"])
def profile():
    return render_template("profile.html")

