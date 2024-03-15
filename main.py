from flask import Flask, render_template, request, redirect
from datetime import datetime
from uuid import uuid4

from app.database.mongo import db

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

@app.route('/users/<name>/links', methods=['POST'])
def add_link(name: str):
  user = db.users.find_one({'name': name})
  link = fields_from_request_form(['url', 'title'], request.form)
  if 'links' not in user:
    user['links'] = []
  link['created_at'] = datetime.now()
  link['id'] = uuid4()
  user['links'].append(link)
  db.users.update_one({'_id': user['_id']}, {'$set': user})
  return render_template('profile.html', user=user)

@app.route('/users/<username>/links/<link_id>', methods=['DELETE'])
def delete_link(username: str, link_id: str):
  user = db.users.find_one({'name': username})
  user['links'] = [link for link in user['links'] if str(link['id']) != link_id]
  db.users.update_one({'_id': user['_id']}, {'$set': user})
  return render_template('profile.html', user=user)
