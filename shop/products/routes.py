from flask import render_template,session, request,redirect,url_for,flash,current_app
from shop import app, db, photos, start_timer, stop_timer
from .models import Category,Brand,Addproduct
from .models import SoldProducts
from .forms import Addproducts
import secrets
import os
from flask_login import current_user
import random
import grpc
from shop import grpc_client
from ..customers.model import Register, Rating
from shop.grpc_server.onlineshopping_pb2 import SearchProductRequestByDesc, SearchProductResponse, GetCartRequest


def brands():
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    return brands

def categories():
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return categories



@app.route('/')
def home():
    resp_time = start_timer()
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=8)
    stop_timer(resp_time, "getHomePage")
    return render_template('products/index.html', products=products,brands=brands(),categories=categories())

@app.route('/result')
def result():
    resp_time = start_timer()
    searchword = request.args.get('q')
    s = SearchProductRequestByDesc(searchword=searchword)
    test = grpc_client.getProductsBySearchword(s)
    for x in test.products: print(x)
    # products = Addproduct.query.msearch(searchword, fields=['name','desc'] , limit=6)
    stop_timer(resp_time, "searchProducts")
    return render_template('products/result.html',products=test.products,brands=brands(),categories=categories())

def getAvgRatingCount(name):
    rating = Rating.query.filter_by(sellername=name).all()
    if(len(rating) > 0):
        like = 0
        for r in rating:
            if r.rating == 1:
                like += 1
        return like
    else:
        return "No rating yet"

@app.route('/product/<int:id>')
def single_page(id):
    resp_time = start_timer()
    product = Addproduct.query.get_or_404(id)
    seller = SoldProducts.query.filter_by(product=product.name).first()
    if(seller == None):
        return render_template('products/single_page.html', product=product, brands=brands(), categories=categories(),
                               seller="unknown", avgrating="No rating")
    else:
        avgRating = getAvgRatingCount(seller.name)
    stop_timer(resp_time, "getProductDetails")
    return render_template('products/single_page.html',product=product,brands=brands(),categories=categories(),seller = seller.name, avgrating=avgRating)




@app.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page',1, type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    brand = Addproduct.query.filter_by(brand=get_brand).paginate(page=page, per_page=8)
    return render_template('products/index.html',brand=brand,brands=brands(),categories=categories(),get_brand=get_brand)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page',1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(page=page, per_page=8)
    return render_template('products/index.html',get_cat_prod=get_cat_prod,brands=brands(),categories=categories(),get_cat=get_cat)


@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method =="POST":
        getbrand = request.form.get('brand')
        id=random.randint(0, 10000)
        brand = Brand(id=id, name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method =="POST":
        getcat = request.form.get('category')
        id=random.randint(0, 10000)
        category = Category(id= id, name=getcat)
        db.session.add(category)
        flash(f'The brand {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')


@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)



@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))


@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    resp_time = start_timer()
    if not session:
        return "please login first"
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        id =  random.randint(0, 10000)
        seller_id = random.randint(0, 10000)
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(id=id,  name=name, price=price, discount=discount, stock=stock, colors=colors, desc=description, category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        db.session.commit()
        if current_user.is_authenticated:
            sellername= current_user.name
            soldproducts = SoldProducts(id=id, name=sellername, email=current_user.email, product=name, quantity_sold=0, stock=stock)
            print(soldproducts)
            db.session.add(soldproducts)
            db.session.commit()
        flash(f'The product {name} was added in database','success')
        stop_timer(resp_time, "addProduct")
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,categories=categories)


@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    resp_time = start_timer()
    if not session:
        return "please login first"
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.colors = form.colors.data
        product.desc = form.description.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        if current_user.is_authenticated:
            sellername= current_user.name
            if not SoldProducts.query.filter_by(name=sellername):
                soldproducts = SoldProducts(name=sellername, email=current_user.email, product=product.name, quantity_sold=0)
                print(soldproducts)
                db.session.add(soldproducts)
                db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.desc
    brand = product.brand.name
    category = product.category.name
    stop_timer(resp_time, "updateProduct")
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)

@app.route('/deleteproduct/<int:id>', methods=['GET','POST'])
def deleteproduct(id):
    print("I am here to delete")
    # product = Addproduct.query.get_or_404(id)
    product = Addproduct.query.get_or_404(id)

    print("I am here to delete")
    if request.method =="POST":
        try:
            print("I am here to unlink")
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        # deleted_objects = addproduct.__table__.delete().where(addproduct.id.in_([id]))
        # session.execute(deleted_objects)
        # session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('admin'))

    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))
