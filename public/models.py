from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
      return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "password":self.password
      }
    #hashes the password parameter and stores it in the object
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    #Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    #To String method
    def __repr__(self):
        return '<User {}>'.format(self.username)  


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(5), unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)

    def toDict(self):
      return {
        "id": self.id,
        "ingredients": self.ingredients,
        "quantity": self.quantity
      }

      def authenticate(ingredient, quantity):
          #search for the specified user
          item = Item.query.filter_by(ingredients=ingredient).first()
          
          if item and item.check_password(ingredient):
            return item
