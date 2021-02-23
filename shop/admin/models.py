from shop import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180),unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False,default='profile.jpg')
    # products = db.Column(db.String(180),unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class SellerProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(500),unique=False, nullable=False)
    email= db.Column(db.String(500),unique=False, nullable=False)
    products = db.Column(db.String(500),unique=False, nullable=False)

    def __repr__(self):
        return 'products you hold: %r' % self.products

    # def getprod(self):
    #     return self.products


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    sellername= db.Column(db.String(50), unique= False)
    product= db.Column(db.String(50), unique= False)
    rating = db.Column(db.Integer, unique= False)

db.create_all()