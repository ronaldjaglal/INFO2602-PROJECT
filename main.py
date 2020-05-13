main import json
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from models import db

def create_app():
    app=Flask(__name__, static_url_path="")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
    db.init_app(app)
    return app

app= create_app()

app.app_context().push()

#getting list of recipes
@app.route('/', methods=['GET'])
def index():
    recipes= Recipes
    return render_template('index.html', recipes= recipes)

def client_app():
  
  return app.send_static_file('app.html')

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)