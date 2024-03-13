from flask import Flask, render_template, request, redirect
from datetime import datetime
from App.mongo import db

app = Flask(__name__)

def fields_from_request_form(field_names, request_form):
  return {
    field: request_form[field] for field in field_names
  }

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/red-alert', methods=['DELETE'])
def red_alert():
  db.users.delete_many({})
  return '<p>Deleted all users</p>'

@app.route('/users', methods=['GET'])
def get_all_users():
  users = list(db.users.find())
  print(users)
  return render_template('users.html', users=users)

@app.route('/users', methods=['POST'])
def create_profile():
  create_user_fields = ['name', 'email']
  user = fields_from_request_form(create_user_fields, request.form)
  user['created_at'] = datetime.now()
  print(user)

  db.users.insert_one(user)

  return redirect(f'/p/{user["name"]}')

@app.route('/p/<name>', methods=['GET'])
def profile(name: str):
  user = db.users.find_one({'name': name})
  print(user)
  return render_template('profile.html', user=user)
