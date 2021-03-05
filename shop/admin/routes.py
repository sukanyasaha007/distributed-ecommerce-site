import random

from flask import render_template,session, request,redirect,url_for,flash
from shop import app, db, bcrypt, grpc_client
from .forms import LoginForm
# from .models import User
from .models import SellerProducts
from shop.products.models import SoldProducts
from shop import start_timer, stop_timer


from shop.products.models import Addproduct,Category,Brand
import zeep
import time
from flask_login import current_user, logout_user, login_user, login_required

from ..customers.forms import CustomerRegisterForm, CustomerLoginFrom
from ..customers.model import Register, Rating
from ..grpc_server.onlineshopping_pb2 import AccountCreationRequest, AccountLoginRequest


@app.route('/admin')
def admin():
    resp_time= start_timer()
    products = Addproduct.query.all()
    stop_timer(resp_time, "seller_landing_page_loading")
    return render_template('admin/index.html', title='Admin page',products=products)

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


@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    resp_time= start_timer()
    form = CustomerLoginFrom()
    try:
        if form.validate_on_submit():
            resp_time = start_timer()
            input_request = AccountLoginRequest(buyer_username=form.email.data, buyer_password=form.password.data)
            # user = Register.query.filter_by(email=form.email.data).first()
            user = grpc_client.login(input_request)
            newUser = Register(id=user.buyer_id, name=user.buyer_name, username=user.buyer_username,
                                email=user.buyer_email, password=user.buyer_password, country=user.buyer_country,
                                city=user.buyer_city, contact=user.buyer_contact, address=user.buyer_address,
                                zipcode=user.buyer_zipcode, itemspurchased=user.items_purchased)
            stop_timer(resp_time, "admin_login")
            print("i am outside of active")
            # session.
            if user.is_active == "true":
                print("i am inside of active")
                login_user(newUser)
                flash('You are login now!', 'success')
                return redirect(url_for('admin'))
            else:
                flash('Incorrect email and password', 'danger')
                return redirect(url_for('admin_login'))
    except Exception as e:
        print(e)
    return render_template('admin/login.html',title='Login page',form=form)

@app.route('/seller/productslist', methods=['GET','POST'])
def seller_products():
    resp_time= start_timer()
    if current_user.is_authenticated:
        name= current_user.name
        products= SellerProducts.query.filter_by(name= name).all()
        # products_= SellerProducts.query.filter_by(name= name).getprod()
        print('products', products)
        # print(products_)
        stop_timer(resp_time, "seller_products_view")
        return render_template('admin/seller_products.html', title='Seller Products', products=products, name= name)
        

def getRatingCount(name):
    rating = Rating.query.filter_by(sellername=name).all()
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
# @login_required
def sold_products():
    resp_time= start_timer()
    print(current_user)
    if current_user.is_authenticated:
        name= current_user.name
        soldproducts= SoldProducts.query.filter_by(name= name).all()
        like, dislike = getRatingCount(name)
        sold_quant={}
        current_stock= {}
        # for s in soldproducts:
        #     print("soldproducts: ",s.name, 'product:', s.product, 'quantity sold:', s.quantity_sold, 'stock')#, s.stock)
        #     sold= s.get_sold(sellername= s.name, prod= s.product)
        #     sold_quant[s.product]= s.quantity_sold
        #     stock_prod= Addproduct.query.filter_by(name=s.product).first()
        #     current_stock[s.product]=stock_prod.stock
        # print(current_stock)
        # stop_timer(resp_time, "view_sold_products")
        # return render_template('admin/sold_products.html', title='Sold Products', name= name, sold=sold_quant, current_stock= current_stock)#, product=soldproducts.product)

        
        if(len(soldproducts) > 0):
            for s in soldproducts:
                print("soldproducts: ",s.name, 'product:', s.product, 'quantity sold:', s.quantity_sold, 'stock')#, s.stock)
                sold= s.get_sold(sellername= s.name, prod= s.product)
                sold_quant[s.product]= s.quantity_sold
                stock_prod= Addproduct.query.filter_by(name=s.product).first()
                current_stock[s.product]=stock_prod.stock
            print(current_stock)
            stop_timer(resp_time, "view_sold_products")
            return render_template('admin/sold_products.html', title='Sold Products', name= name, sold=sold_quant, current_stock= current_stock, like=like, dislike=dislike)#, product=soldproducts.product)
        else:
            flash("You have sold products, sorry!", 'danger')
            redirect(url_for('admin'))


@app.route('/seller/logout')
def seller_logout():
    resp_time= start_timer()
    logout_user()
    session.clear()
    stop_timer(resp_time, "seller_logout")
    return redirect(url_for('admin'))