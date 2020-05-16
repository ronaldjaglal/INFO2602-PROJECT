 import json
from flask import Flask, request, render_template, url_for, redirect, session, flash
from functools import wraps
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''

''' Set up JWT here '''
def authenticate(uname, password):
  #search for the specified user
  user = User.query.filter_by(username=uname).first()
  #if user is found and password matches
  if user and user.check_password(password):
    return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)

''' End JWT Setup '''


''' Login '''
#def login_required(f):
 # @wraps(f)
  #def wraps (*args,**kwargs):
   # if 'logged_in' in sessions:
    #  return f(*args, **kwargs)
    #else:
     # flash('you need to login first.')
      #return redirect(url_for('login'))
  #return wrap
 
@app.route('/logout')
#@login_required
def index():
   return render_template("logout.html") 
  
@app.route('/home')
def welcome():
  return render_template("home.html") 

@app.route ('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
      if request.form['username'] != 'admin' or request.form ['password'] != 'admin':
         error = 'Invalid credentials.  Please try again.'
      else:
        session ['logged_in']= True;
        flash('You were just logged in.')
        return redirect(url_for('index'))
    return render_template("login.html", error=error)

@app.route ('/logout')
def logout():
    session.pop ('logged_in', None)
    flash('You were just logged out.')
    return redirect(url_for('welcome'))
  

@app.route('/signup', methods=['POST'])
def signup():
  userdata = request.get_json() # get userdata
  newuser = User(username=userdata['username'], email=userdata['email']) # create user object
  newuser.set_password(userdata['password']) # set password
  try:
    db.session.add(newuser)
    db.session.commit() # save user
  except IntegrityError: # attempted to insert a duplicate user
    db.session.rollback()
    return 'username or email already exists' # error message
  return 'user created' # success

''' Item ''' 
@app.route('/items')
def index():
    pie = Item(ingredients="sugar",quantity=5)
    salad = Item(ingredients="lettuce",quantity=6)
    Items = [pie.toDict(), salad.toDict()]
    db.session.add(pie)
    db.session.add(salad)
    db.session.commit
    item = Item.query.get(1)
    return json.dumps(Items)

app.run(host='0.0.0.0', port=8080)
