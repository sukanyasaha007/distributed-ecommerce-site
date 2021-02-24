from shop import db
from datetime import datetime

from werkzeug.exceptions import HTTPException


class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')
    keywords = db.Column(db.Text, default='product')
    condition = db.Column(db.Text, default='product')



    def __repr__(self):
        return '<Post %r>' % self.name


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Brand %r>' % self.name
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name


class SoldProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(500),unique=False, nullable=False)
    email= db.Column(db.String(500),unique=False, nullable=False)
    product = db.Column(db.String(500),unique=False, nullable=False)
    quantity_sold= db.Column(db.Integer, nullable=False)
    # stock= db.Column(db.Integer, nullable=False)

    def get_sold(self, sellername, prod):
        self.sellername= sellername
        if self.sellername== self.name:
            if self.product== prod:
                return self.quantity_sold
    def update_stock(self, sellername, prod, quantity_sold):
        self.sellername= sellername
        if not self.sellername== self.name:
            raise HTTPException(code=415)
        else:
            if self.product== prod:
                self.quantity_sold+= quantity_sold
                # self.stock-= self.stock
                return quantity_sold

    def __repr__(self):
        return '<Catgory %r>' % self.name
        # return instance
    # def __repr__(self):
    #     return 'product {} sold {}'.format(self.product, self.quantity_sold)


db.create_all()

# SoldProducts().get_or_415(name='Sukanya Saha')