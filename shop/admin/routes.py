import random

from flask import render_template,session, request,redirect,url_for,flash, jsonify, make_response
from shop import app, db, bcrypt, grpc_client,grpc_client_seller
from .forms import LoginForm
# from .models import User
from .models import SellerProducts
from shop.products.models import SoldProducts
from shop import start_timer, stop_timer


from shop.products.models import Addproduct,Category,Brand
import zeep
import time
# from flask_login import current_user, logout_user, login_user, login_required
from google.protobuf.json_format import MessageToJson

from ..customers.forms import CustomerRegisterForm, CustomerLoginFrom
from ..customers.model import Register, Rating
from ..grpc_server.onlineshopping_pb2 import AccountCreationRequest, AccountLoginRequest


from ..grpc_server.seller_pb2 import SellerAddProductsRequest

import jwt

def auth_required(fn):
    def decorated(**kwargs):
        print("Inside Auth Required")
        authToken = request.cookies.get("authToken")
        authData = {
            "isAuthenticated": False,
            "userName": None,
            "email" : None,
            "name": None
        }

        if authToken:
            try:
                jwtData = jwt.decode(jwt=authToken, key=app.config["JWT_SECRET_KEY"], verify=True, algorithms="HS256")
                print(jwtData)
                authData["isAuthenticated"] = True
                authData["userName"] = jwtData["user_name"]
                authData["email"] = jwtData["email"]
                authData["name"] = jwtData["name"]

            except Exception as e:
                print("jwt varification failed: ", e)
        else:
            print("No token found")
        return fn(authData, **kwargs)
    decorated.__name__ = fn.__name__
    return decorated

@app.route('/admin')
@auth_required
def admin(authData):
    resp_time= start_timer()
    if authData["isAuthenticated"]:
        name= authData["userName"]
        # seller_data= Register.query.filter_by(username= name).first()
        products= Addproduct.query.filter_by(seller= authData["userName"]).all()
    # print(name, products)
    # products = Addproduct.query.all()
        stop_timer(resp_time, "seller_landing_page_loading")
        return render_template('admin/index.html', title='Admin page',products=products)
    else:
        return redirect(url_for("admin_login_page"))

@app.route('/admin/login', methods=['GET'])
def admin_login_page():
    return render_template('admin/login.html',title='Login page')

@app.route('/admin/login', methods=['POST'])
def admin_login():
    resp_time= start_timer()
    try:
        if len(request.json["email"]) and len(request.json["password"]):
            
            input_request = AccountLoginRequest(buyer_username=request.json["email"], buyer_password=request.json["password"])
            # user = Register.query.filter_by(email=form.email.data).first()
            print(input_request)
            user = grpc_client.login(input_request)
            if user.buyer_username == '' or user== None:
                print("Invalid userid or password")
                return jsonify({'message': "Invalid userid or password"}), 401
            newUser = Register(id=user.buyer_id, name=user.buyer_name, username=user.buyer_username,
                                email=user.buyer_email, password=user.buyer_password, country=user.buyer_country,
                                city=user.buyer_city, contact=user.buyer_contact, address=user.buyer_address,
                                zipcode=user.buyer_zipcode, itemspurchased=user.items_purchased)
            stop_timer(resp_time, "admin_login")
            token = jwt.encode({"user_name": user.buyer_username, "user_type": "seller", "email" : request.json["email"], "name": user.buyer_name}, app.config["JWT_SECRET_KEY"], algorithm="HS256")
            session["logged_in"]=True
            # if user.is_active == "true":
            #     login_user(newUser)
            #     flash('You are logged in now!', 'success')
            #     stop_timer(resp_time, "adminLogin")
            resp = make_response(MessageToJson(user))
            resp.set_cookie("authToken", token, httponly=True, samesite="Lax")
            # return resp
            return resp;
            # return jsonify({'token' : token.decode('UTF-8')})
        else:
            flash('Incorrect email and password', 'danger')
            return jsonify({'test': 123}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500

@app.route('/admin/brands')
def brands():
    resp_time= start_timer()
    brands = Brand.query.order_by(Brand.id.desc()).all()
    stop_timer(resp_time, "seller_brand")
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/admin/categories')
def categories():
    resp_time= start_timer()
    categories = Category.query.order_by(Category.id.desc()).all()
    stop_timer(resp_time, "seller_cat")
    return render_template('admin/brand.html', title='categories',categories=categories)

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        resp_time = start_timer()
        input_request = AccountCreationRequest \
            (buyer_id=random.randint(0, 10000),
             buyer_name=form.name.data,
             buyer_email=form.email.data,
             buyer_username=form.username.data,
             buyer_password=form.password.data,
             items_purchased=0,
             buyer_city=form.city.data,
             buyer_contact=form.contact.data,
             buyer_address=form.address.data,
             buyer_country=form.country.data,
             buyer_zipcode=form.zipcode.data,
             )
        response = grpc_client.createAccount(input_request)
        stop_timer(resp_time, "sellerCreateAccount")
        if (response.status == "success"):
            flash(f'Welcome {form.name.data} Thank you for registering! Login now', 'success')
            return redirect(url_for('admin_login'))
        else:
            flash(f'Error in registering for {form.name.data}. Try again', 'danger')
            return redirect(url_for('adminRegister'))

    return render_template('customer/register.html', form=form)


@app.route('/seller/productslist', methods=['GET','POST'])
@auth_required
def seller_products(authData):
    resp_time= start_timer()
    if authData["isAuthenticated"]:
        name= authData["userName"]
        products= SellerProducts.query.filter_by(name= name).all()
        # products_= SellerProducts.query.filter_by(name= name).getprod()
        print('products', products)
        # print(products_)
        stop_timer(resp_time, "seller_products_view")
        return render_template('admin/seller_products.html', title='Seller Products', products=products, name= name)

def getRatingCount(name):
    rating = Rating.query.filter_by(sellername=name).all()
    print("Ratinggggg", name)
    if(len(rating) > 0):
        like = 0
        dislike = 0
        for r in rating:
            if r.rating == 1:
                like += 1
            else:
                dislike +=1
        return like, dislike
    else:
        return 0, 0

@app.route('/seller/soldproducts', methods=['GET','POST'])
@auth_required
def sold_products(authData):
    resp_time= start_timer()
    if authData["isAuthenticated"]:
        name = authData["userName"]
        email = authData["email"]
        print("Inside soldproducts")
        soldproducts= SoldProducts.query.filter_by(email= email).all()
        print(soldproducts)
        print("after query for solditems", soldproducts)
        like, dislike = getRatingCount(authData["name"])
        sold_quant={}
        current_stock= {}
        if(len(soldproducts) > 0):
            for s in soldproducts:
                print("soldproducts: ",s.name, 'product:', s.product, 'quantity sold:', s.quantity_sold, 'stock:' , s.stock)#, s.stock)
                sold= s.get_sold(sellername= s.name, prod= s.product)
                sold_quant[s.product]= s.quantity_sold
                stock_prod= Addproduct.query.filter_by(name=s.product).first()
                if stock_prod== None:
                    # flash("You have sold products, sorry!", 'danger')
                    redirect(url_for('admin'))
                else:
                    current_stock[s.product]=stock_prod.stock
            print(current_stock)
            stop_timer(resp_time, "view_sold_products")
            return render_template('admin/sold_products.html', title='Sold Products', name= name, sold=sold_quant, current_stock= current_stock, like=like, dislike=dislike)#, product=soldproducts.product)
        else:
            print("I am inside print of else")
            flash("You have sold products, sorry!", 'danger')
            return redirect(url_for('admin'))


@app.route('/seller/logout', methods=['DELETE'])
@auth_required
def seller_logout(authData):
    if authData["isAuthenticated"]:
        resp = make_response()
        resp.set_cookie("authToken", expires=0)
        return resp;
    return jsonify({'message': "User not logged in"}), 400
