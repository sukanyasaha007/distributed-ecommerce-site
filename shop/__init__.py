from flask_socketio import SocketIO

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_uploads import UploadSet
from flask_uploads import configure_uploads
from flask_uploads import IMAGES, patch_request_class
import os
import time
import csv

from flask_msearch import Search
from flask_login import LoginManager, logout_user
from flask_migrate import Migrate

import grpc
from shop.grpc_server.onlineshopping_pb2_grpc import BuyerActionsStub

from shop.grpc_server.seller_pb2_grpc import SellerStub

# jwt
from flask_restful import Api
# from flask_jwt_extended import JWTManager
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/onlineshopping'

# app.config['SQLALCHEMY_DATABASE_URI']= 'cockroachdb://admin:abc%40123@35.209.30.130:25262/onlineshopping?sslmode=disable'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_CONNECTION_STRING")

# LATENCY_REPORT_PATH="/Users/sukanyasaha/Desktop/Distributed Systems/Assignments/Assignment4/distributed-system-assignment2/latencyreport.csv"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:my-secret-pw@host.docker.internal:3306/onlineshopping'
app.config['SECRET_KEY']='djshakuo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
# UploadSet('photos', default_dest=IMAGES app: app.instance_root)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
# db.session.rollback()
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)
socketio = SocketIO(app)

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "mysql":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"
soap_host = ""
#GRPC params
# channel = grpc.secure_channel("grpc-server-vlhiisghja-uc.a.run.app:443", grpc.ssl_channel_credentials())
# channel = grpc.insecure_channel("host.docker.internal:50051")
channel = grpc.insecure_channel("[::]:50051")

grpc_client = BuyerActionsStub(channel)
grpc_client_seller= SellerStub(channel)
socketio = SocketIO(app)

@socketio.on('disconnect')
def disconnect_user():
    logout_user()

def start_timer():
    start_time = time.time()
    return start_time

# "/Users/sukanyasaha/Desktop/Distributed Systems/Assignments/Assignment 2/Namratha/V3/distributed-system-assignment2/run.py"
def stop_timer(start_time, funct):
    # output is in seconds
    resp_time = (time.time() - start_time)
    with open(os.environ.get("LATENCY_REPORT_PATH"), 'a', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([funct, str(resp_time)])
    return

from shop.products import routes
from shop.admin import routes
from shop.carts import carts
from shop.customers import routes

from flask import request

# app.config['BASE_URL'] = 'http://0.0.0.0:5000'  #Running on localhost
app.config['JWT_SECRET_KEY'] = 'onlineshopping'  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True

app.config['SESSION_COOKIE_HTTPONLY']=True
app.config['REMEMBER_COOKIE_HTTPONLY']=True
app.config['BASE_URL']= "http://127.0.0.1:5000"
# jwt = JWTManager(app)

