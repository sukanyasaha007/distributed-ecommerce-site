from sqlalchemy import Column, String, Integer, Date, Numeric, \
    Text, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# engine = create_engine('mysql+pymysql://root:my-secret-pw@host.docker.internal:3306/onlineshopping')
Base = declarative_base()

class Register(Base):
    __tablename__ = 'register'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(200), unique=False)
    country = Column(String(50), unique=False)
    # state = db.Column(db.String(50), unique= False)
    city = Column(String(50), unique=False)
    contact = Column(String(50), unique=False)
    address = Column(String(50), unique=False)
    zipcode = Column(String(50), unique=False)
    profile = Column(String(200), unique=False, default='profile.jpg')
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    itemspurchased = Column(Integer, unique=False)

    def __init__(self, id, name, username, email, password, country, city, contact,
                 address, zipcode, profile, date_created, itemspurchased):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.country = country
        self.city = city
        self.contact = contact
        self.address = address
        self.zipcode = zipcode
        self.profile = profile
        self.date_created = date_created
        self.itemspurchased = itemspurchased

class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Addproduct(Base):
    __tablename__ = 'addproduct'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    discount = Column(Integer, default=0)
    stock = Column(Integer, nullable=False)
    colors = Column(Text, nullable=False)
    desc = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False,default=datetime.utcnow)

    category_id = Column(Integer, ForeignKey('category.id'),nullable=False)
    category = relationship('Category',backref='categories')

    brand_id = Column(Integer, ForeignKey('brand.id'),nullable=False)
    brand = relationship('Brand',backref='brands')

    image_1 = Column(String(150), nullable=False, default='image1.jpg')
    image_2 = Column(String(150), nullable=False, default='image2.jpg')
    image_3 = Column(String(150), nullable=False, default='image3.jpg')
    keywords = Column(Text, default='product')
    condition = Column(Text, default='product')

    def __init__(self, id, name, price, discount, stock, colors, desc, pub_date, category_id,
                 category, brand_id, brand, image_1, image_2, image_3):
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.colors = colors
        self.desc = desc
        self.pub_date = pub_date
        self.category_id = category_id
        self.category = category
        self.brand_id = brand_id
        self.brand = brand
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3

    def getDict(self, obj):
        return obj.__dict__

class cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=True)
    customer_id = Column(Integer, nullable=True)
    name = Column(String(80), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    discount = Column(Integer, default=0)
    stock = Column(Integer, nullable=False)
    colors = Column(Text, nullable=False)
    descp = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False,default=datetime.utcnow)

    image_1 = Column(String(150), nullable=False, default='image1.jpg')
    image_2 = Column(String(150), nullable=False, default='image2.jpg')
    image_3 = Column(String(150), nullable=False, default='image3.jpg')

    def __init__(self, id, product_id, customer_id, name, price, discount, stock, colors, desc, pub_date
                 , image_1, image_2, image_3):
        self.id = id
        self.product_id = product_id
        self.customer_id = customer_id
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.colors = colors
        self.descp = desc
        self.pub_date = pub_date
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3