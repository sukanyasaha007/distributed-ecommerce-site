from flask import render_template,session, redirect,url_for,flash, make_response, jsonify
from flask_login import login_required, current_user, logout_user, login_user
from shop import app,db, soap_host
from .forms import CustomerRegisterForm, CustomerLoginFrom, RatingForm
from .model import Register, CustomerOrder, Rating
from shop.products.models import Addproduct, SoldProducts
from shop.carts.carts import clearcart
from shop import start_timer, stop_timer
import random
import secrets
import pdfkit
import stripe
import zeep
import time
from google.protobuf.json_format import MessageToJson
from ..products.routes import brands, categories
from shop.grpc_server.onlineshopping_pb2 import AccountCreationRequest, AccountLoginRequest

from shop.grpc_server.onlineshopping_pb2 import AccountCreationRequest, AccountLoginRequest, GetCartRequest

from flask import request
from shop import grpc_client
import jwt

buplishable_key ='pk_test_51IN5nDCVZ5Yf06wRG9BLSKuBUaUqXKWKxbQPjAtHcsYdZgY0NiTG0aXIf25Ll29ItyhvnxjBa1FSUJPCo107MmCD00nkqBkcID'
stripe.api_key ='sk_test_51IN5nDCVZ5Yf06wROWN3sRW7aVEhhCfo3obH4jNrU1MuzrOVeLS03hIwbs3UHOcL0v356Z01J1eP8rpcOZT6tQjF00HLVt218C'

def auth_required_buyer(fn):
    def decorated(**kwargs):
        # print("Inside Auth Required")
        authToken = request.cookies.get("authToken")
        authData = {
            "isAuthenticated": False,
            "userName": None,
            "userId": None
        }

        if authToken:
            try:
                jwtData = jwt.decode(jwt=authToken, key=app.config["JWT_SECRET_KEY"], verify=True, algorithms="HS256")
                # print("jwtData", jwtData)
                authData["isAuthenticated"] = True
                authData["userName"] = jwtData["user_name"]
                authData["userId"] = jwtData["user_id"]

            except Exception as e:
                print("jwt varification failed: ", e)
        else:
            print("No token found")
        return fn(authData, **kwargs)
    decorated.__name__ = fn.__name__
    return decorated
    

@app.route('/payment',methods=['POST'])
@auth_required_buyer
def payment(authData):
    resp_time = start_timer()
    invoice = request.form.get('invoice')
    amount = request.form.get('amount')
    customer = stripe.Customer.create(
      email=request.form['stripeEmail'],
      source=request.form['stripeToken'],
    )
    # charge = stripe.Charge.create(
    #   customer=customer.id,
    #   description='Myshop',
    #   amount=amount,
    #   currency='usd',
    # )
    buyer_data= Register.query.filter_by(username= authData["userName"]).first()
    # print("buyer_data.id", buyer_data.id)
    orders =  CustomerOrder.query.filter_by(invoice=invoice).order_by(CustomerOrder.id.desc()).first()
    orders.status = 'Paid'
    db.session.commit()
    result = makeTransaction(order=invoice)
    if result:
        for key, prod in orders.orders.items():
            product = Addproduct.query.get_or_404(key)
            product.stock = product.stock - prod['quantity']
            db.session.commit()
            soldproducts= SoldProducts.query.filter_by(product=product.name).first()
            soldproducts.update_stock(sellername=soldproducts.name, prod=product.name, quantity_sold=prod['quantity'])
            # prods[seller.name]= product.name
            clearcart()
            db.session.commit()

            stop_timer(resp_time, "makePayment")
    return redirect(url_for('thanks'))


def makeTransaction(order):
    # resp_time = start_timer()
    # transport = zeep.Transport(cache=None)
    # client = zeep.Client(soap_host+"/?WSDL", transport=transport)
    # result = client.service.slow_request()
    # stop_timer(resp_time, "soapServer")
    return True

@app.route('/thanks')
def thanks():
    return render_template('customer/thank.html')

@app.route('/rating/<seller>/<product>', methods=['GET','POST'])
def rating(seller, product):
    resp_time = start_timer()
    form= RatingForm()
    if form.validate_on_submit():
        id = random.randint(0, 10000)
        rating= Rating(id=id, product=product, rating=form.rating.data, sellername=seller)
        db.session.add(rating)
        flash(f'Thank you for submitting your rating', 'success')
        db.session.commit()
        stop_timer(resp_time, "rateSeller")
        return redirect(url_for('displayOrders'))
    return render_template('customer/rating.html', form=form, product=product, seller=seller)

@app.route('/customer/register', methods=['GET','POST'])
def customer_register():
    resp_time = start_timer()
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        input_request = AccountCreationRequest \
            (buyer_id=random.randint(0, 10000),
             buyer_name=form.name.data,
             buyer_email=form.email.data,
             buyer_username=form.username.data,
             buyer_password=form.password.data,
             items_purchased = 0,
             buyer_city=form.city.data,
             buyer_contact=form.contact.data,
             buyer_address=form.address.data,
             buyer_country=form.country.data,
             buyer_zipcode=form.zipcode.data,
             )
        # register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        response = grpc_client.createAccount(input_request)
        # db.session.add(register)
        stop_timer(resp_time, "buyerCreateAccount")
        if(response.status == "success"):
            flash(f'Welcome {form.name.data} Thank you for registering! Login now', 'success')
            return redirect(url_for('customerLogin'))

        # db.session.commit()
        else:
            flash(f'Error in registering for {form.name.data}. Try again', 'danger')
            return redirect(url_for('customerRegister'))
    return render_template('customer/register.html', form=form)
@app.route('/')
@auth_required_buyer
def home(authData):
    resp_time = start_timer()
    length_existing = 0
    page = request.args.get('page',1, type=int)
    # if authData["isAuthenticated"]:
    name= authData["userName"]
    # seller_data= Register.query.filter_by(username= name).first()
    # products= Addproduct.query.filter_by(seller= seller_data.name).all()
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=8)
    # print("check1",authData, products)
    if(authData["userId"] != None):
        existing = grpc_client.getFromcart(GetCartRequest(customerId=str(authData["userId"])))
        length_existing = len(existing.products)
    else:
        length_existing = 0
    stop_timer(resp_time, "getHomePage")
    return render_template('products/index.html', products=products,brands=brands(),categories=categories(), user=name,
                           noItems=length_existing)
    # else:
    #     return redirect(url_for("customer_login_page"))

@app.route('/customer/login', methods=['GET'])
def customer_login_page():
    # print("Inside customer login page func")
    return render_template('customer/login.html',title='Login page')

@app.route('/customer/login', methods=['POST'])
def customerLogin():
    resp_time = start_timer()
    # form = CustomerLoginFrom()
    try:
        if len(request.json["email"]) and len(request.json["password"]):
            input_request = AccountLoginRequest(buyer_username=request.json["email"], buyer_password=request.json["password"])
            # print("check 2", input_request)
            user = grpc_client.login(input_request)
            # print("check 3", user)
            if user.buyer_username == '' or user== None:
                # print("Invalid userid or password")
                return jsonify({'message': "Invalid userid or password"}), 401
            # print("I am inside customer login")
            newUser = Register(id=user.buyer_id, name=user.buyer_name, username=user.buyer_username,
                                email=user.buyer_email, password=user.buyer_password, country=user.buyer_country,
                                city=user.buyer_city, contact=user.buyer_contact, address=user.buyer_address,
                                zipcode=user.buyer_zipcode, itemspurchased=user.items_purchased)
            token = jwt.encode({"user_name": user.buyer_username, "user_type": "seller", "user_id": user.buyer_id}, app.config["JWT_SECRET_KEY"], algorithm="HS256")
            session["logged_in"]=True
            resp = make_response(MessageToJson(user))
            resp.set_cookie("authToken", token, httponly=True, samesite="Lax")
            stop_timer(resp_time, "buyer_login")
            # print("check 4", resp, token)
            return resp;
        else:
            flash('Incorrect email and password', 'danger')
            return jsonify({'test': 123}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


@app.route('/customer/logout', methods=["DELETE"])
@auth_required_buyer
def customer_logout(authData):
    if authData["isAuthenticated"]:
        resp = make_response()
        resp.set_cookie("authToken", expires=0)
        return resp;
    return jsonify({'message': "User not logged in"}), 400

def updateshoppingcart():
    for key, shopping in session['Shoppingcart'].items():
        session.modified = True
        del shopping['image']
        del shopping['colors']
    return updateshoppingcart

@app.route('/getorder')
@auth_required_buyer
def get_order(authData):
    resp_time = start_timer()
    if authData["isAuthenticated"]:
        buyer_data = authData
        invoice = secrets.token_hex(5)
        id = random.randint(0, 100000)
        cartDisplay = {}
        prd = {}
        # print("session>>>>>>>",session['Shoppingcart'])
        updateshoppingcart
        try:
            existing = grpc_client.getFromcart(GetCartRequest(customerId=str(buyer_data["userId"])))
            if len(existing.products) == 0:
                return redirect(url_for('home'))

            for i in existing.products:
                prd[i.id] = {'color': i.colors, 'colors': i.colors,
                            'discount': i.discount, 'image': i.image_1, 'name': i.name,
                            'price': float(i.price), 'quantity': i.stock}
            cartDisplay['Shoppingcart'] = prd
            order = CustomerOrder(id=id, invoice=invoice,customer_id=buyer_data["userId"],orders=cartDisplay['Shoppingcart'])
            # print("order>>>>>>>>>>", order.invoice)
            db.session.add(order)
            db.session.commit()
            # session.pop('Shoppingcart')
            flash('Your order has been sent successfully','success')
            stop_timer(resp_time, "getorder")
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
            print(e)
            flash('Some thing went wrong while get order', 'danger')
            return redirect(url_for('getCart'))
        


@app.route('/orders/<invoice>')
@auth_required_buyer
def orders(authData, invoice):
    resp_time = start_timer()
    if authData["isAuthenticated"]:
        grandTotal = 0
        subTotal = 0
        customer_id = authData["userId"]
        customer_name = authData["userName"]
        # orders = CustomerOrder.query.filter_by(customer_id = customer_id).all()
        orders= CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
        print("orders?????????????????????", orders)
        for _key, product in orders.orders.items():
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = ("%.2f" % (1.06 * float(subTotal)))
            stop_timer(resp_time, "getFinalOrder")
    else:
        return redirect(url_for('customerLogin'))
    return render_template('customer/order.html', invoice=invoice, tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer_name,orders=orders)

@app.route('/displayorders')
@auth_required_buyer
def displayOrders(authData):
    resp_time = start_timer()
    if authData["isAuthenticated"]:
        sellers = []
        grandTotal = 0
        subTotal = 0
        customer_id = authData["userId"]
        customer = authData["userName"]
        orders = CustomerOrder.query.filter_by(customer_id = customer_id)
        finalOrders = []
        if(orders.count() > 0):
            for k in orders:
                for _key, product in k.orders.items():
                    soldproducts = SoldProducts.query.filter_by(product = product['name']).first()
                    # print(product['name'])
                    if soldproducts != None:
                        finalOrders.append(k)
                        sellers.append(soldproducts.name)
                        discount = (product['discount']/100) * float(product['price'])
                        subTotal += float(product['price']) * int(product['quantity'])
                        subTotal -= discount
                        tax = ("%.2f" % (.06 * float(subTotal)))
                        grandTotal = ("%.2f" % (1.06 * float(subTotal)))
                        stop_timer(resp_time, "displayOrders")
        else:
            flash("You have no orders", 'success')
            return redirect(url_for('home'))

    else:
        return redirect(url_for('customerLogin'))
    return render_template('customer/displayOrders.html', tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer,orders=finalOrders, sellers=sellers, noorders = len(finalOrders))


@app.route('/get_pdf/<invoice>', methods=['POST'])
@auth_required_buyer
def get_pdf(authData, invoice):
    if authData["isAuthenticated"]:
        grandTotal = 0
        subTotal = 0
        customer_id = authData["userId"]
        if request.method =="POST":
            customer = authData["userName"]
            orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
            for _key, product in orders.orders.items():
                discount = (product['discount']/100) * float(product['price'])
                subTotal += float(product['price']) * int(product['quantity'])
                subTotal -= discount
                tax = ("%.2f" % (.06 * float(subTotal)))
                grandTotal = float("%.2f" % (1.06 * subTotal))

            rendered =  render_template('customer/pdf.html', invoice=invoice, tax=tax,grandTotal=grandTotal,customer=customer,orders=orders)
            pdf = pdfkit.from_string(rendered, False)
            response = make_response(pdf)
            response.headers['content-Type'] ='application/pdf'
            response.headers['content-Disposition'] ='inline; filename='+invoice+'.pdf'
            return response
    return request(url_for('orders'))


