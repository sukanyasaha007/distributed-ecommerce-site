from flask import render_template,session, request,redirect,url_for,flash
from shop import app,db,bcrypt
from .forms import RegistrationForm,LoginForm
from .models import User
# from .models import SoldProducts,SellerProducts
from shop.products.models import Addproduct,Category,Brand
import zeep
import time
from flask_login import current_user

@app.route('/admin')
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin page',products=products)

@app.route('/admin/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/admin/categories')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)

        sellerproducts = SellerProducts(name=form.name.data,email=form.email.data, products= form.products.data)
        db.session.add(sellerproducts)
        # print('sellerproducts', sellerproducts)
        # print('db', SellerProducts.query.filter_by(name= form.name.data).all())
        flash(f'welcome {form.name.data} Thanks for registering','success')
        db.session.commit()
        return redirect(url_for('admin_login'))
    return render_template('admin/register.html',title='Register user', form=form)


@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'welcome {form.email.data} you are logedin now','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('admin_login'))
    return render_template('admin/login.html',title='Login page',form=form)



# @app.route('/seller/productslist', methods=['GET','POST'])
# def seller_products():
#     if current_user.is_authenticated:
#         name= current_user.name
#         products= SellerProducts.query.filter_by(name= name).all()
#         # products_= SellerProducts.query.filter_by(name= name).getprod()
#         print('products', products)
#         # print(products_)
#         return render_template('admin/seller_products.html', title='Seller Products', products=products, name= name)
        

# @app.route('/seller/soldproducts', methods=['GET','POST'])
# def seller_products():
#     if current_user.is_authenticated:
#         name= current_user.name
#         products= SoldProducts.query.filter_by(name= name).all()
#         products= SoldProducts.query.filter_by(name= name).all()
#         print('products', products)
#         return render_template('admin/sold_products.html', title='Sold Products', products=products, name= name)
        
