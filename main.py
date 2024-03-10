from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/profile')
def profile():
  user = User('Zac', 'zac@quesofres.co', links=[
    Link('https://quesofres.co', 'Queso Fresco'),
    Link('https://zacmilano.com', 'Personal site'),
  ])
  return render_template('profile.html', user=user)

class User:
  def __init__(self, username, email, links=[]):
    self.username = username
    self.email = email
    self.links = links
    self.created_at = datetime.now()
  
  def withLink(self, url, title):
    return Link(url, title)

class Link:
  def __init__(self, url, title):
    self.url = url
    self.title = title
