from flask import render_template, session, request, redirect, url_for, flash, current_app
from shop import db, app, start_timer, stop_timer
from shop.products.routes import brands, categories
from ..customers.model import Register
from ..products.models import Addproduct
from flask_login import current_user
from shop.grpc_server.onlineshopping_pb2 import SearchProductRequest, AddToCartRequest, UpdateproductQuantity, \
    GetCartRequest, GetCartRequestProd, AccountLoginRequest, ProductDetails, SearchProductResponse
from shop.products.models import cart
from shop import grpc_client
import jwt

def auth_required_buyer(fn):
    def decorated(**kwargs):
        print("Inside Auth Required")
        authToken = request.cookies.get("authToken")
        authData = {
            "isAuthenticated": False,
            "userName": None,
            "userId": None
        }

        if authToken:
            try:
                jwtData = jwt.decode(jwt=authToken, key=app.config["JWT_SECRET_KEY"], verify=True, algorithms="HS256")
                print("jwtData", jwtData)
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
    

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))


@app.route('/addcart', methods=['POST'])
@auth_required_buyer
def AddCart(authData):
    try:
        if authData["isAuthenticated"]:
            print(authData)
            buyer_data = authData
        resp_time = start_timer()
        product_id = request.form.get('product_id')
        print("Inside Addcart",buyer_data["userName"], "\n", product_id)
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        print(product_id)
        # item = SearchProductRequest(product=str(product_id))
        # response = grpc_client.search(item)
        product = Addproduct.query.filter_by(id=product_id).first()
        # product = response.products
        # print("check",item, response)
        if request.method == "POST":
            # DictItems = {
                # product_id: {'name': product[0].name, 'price': float(product[0].price), 'discount': product[0].discount,
                #              'color': color, 'quantity': quantity, 'image': product[0].image_1,
                #              'colors': product[0].colors}}
            DictItems = {product_id:{'name':product.name,'price':float(product.price),
            'discount':product.discount,'color':color,'quantity':quantity,
            'image':product.image_1, 'colors':product.colors}}
            print("check", DictItems)
            existing = grpc_client.getFromcartProd(GetCartRequestProd(customerId=str(buyer_data["userId"]), productId=str(product_id)))
            print(existing)
            if existing!= None and len(existing.products) != 0:
                found = False
                for ex in existing.products:
                    if(product_id == ex.id):
                        found = True
                        grpc_client.updateproductQuantity(UpdateproductQuantity(customer=buyer_data["userId"],
                                                                        product=str(product_id),
                                                                                                quantity=int(quantity+1)))
                if(not found):
                    print("heloooooooooo")
                    # session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    productlistArray = []
                    productlist = ProductDetails()
                    productlist.name = product.name
                    productlist.id = product.id
                    productlist.price = str(product.price)
                    productlist.discount = int(product.discount)
                    productlist.stock = product.stock
                    productlist.colors = product.colors
                    productlist.desc = product.desc
                    productlist.pub_date = str(product.pub_date)
                    productlist.category_id = productlist.category_id
                    productlist.category = str(product.category.name)
                    productlist.brand_id = product.brand_id
                    productlist.brand = str(product.brand.name)
                    productlist.image_1 = product.image_1
                    productlist.image_2 = product.image_2
                    productlist.image_3 = product.image_3
                    productlist.condition = "new"
                    productlistArray.append(productlist)
                    resprod = SearchProductResponse(products=productlistArray)
                    print("Yoooooooooooo")
                    res = grpc_client.addToCart(
                        AddToCartRequest(customerId=str(buyer_data["userId"]), products=resprod))
                    print(res)
                    return redirect(request.referrer)

            # if 'Shoppingcart' in session:
            #     print(session['Shoppingcart'])
            #     if product_id in session['Shoppingcart']:
            #         for key, item in session['Shoppingcart'].items():
            #             if int(key) == int(product_id):
            #                 grpc_client.updateproductQuantity(UpdateproductQuantity(customer=buyer_data.id,
            #                                                   product=str(product_id),
            #                                                                         quantity=int(item['quantity'])+1))
            #                 session.modified = True
            #                 item['quantity'] += 1
            #     else:
            #         session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
            #         grpc_client.addToCart(AddToCartRequest(customerId=str(buyer_data.id), products=product))
            #         return redirect(request.referrer)
            else:
                productlistArray = []
                productlist = ProductDetails()
                productlist.name = product.name
                productlist.id = product.id
                productlist.price = str(product.price)
                productlist.discount = int(product.discount)
                productlist.stock = product.stock
                productlist.colors = product.colors
                productlist.desc = product.desc
                productlist.pub_date = str(product.pub_date)
                productlist.category_id = productlist.category_id
                productlist.category = str(product.category.name)
                productlist.brand_id = product.brand_id
                productlist.brand = str(product.brand.name)
                productlist.image_1 = product.image_1
                productlist.image_2 = product.image_2
                productlist.image_3 = product.image_3
                productlist.condition = "new"
                productlistArray.append(productlist)
                resprod = SearchProductResponse(products = productlistArray)
                res = grpc_client.addToCart(AddToCartRequest(customerId=str(buyer_data["userId"]), products=resprod))
                print(res.status)
                # session['Shoppingcart'] = DictItems
                stop_timer(resp_time, "addTocart")
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/carts')
@auth_required_buyer
def getCart(authData):
    resp_time = start_timer()
    buyer_data = None
    print(authData)
    if authData["isAuthenticated"]:
        print(authData)
        buyer_data= authData
    existing = grpc_client.getFromcart(GetCartRequest(customerId=str(buyer_data["userId"])))
    print("cart contents -> ", existing)
    prd = {}
    cartDisplay = {}
    subtotal = 0
    grandtotal = 0
    if len(existing.products) != 0:
        for i in existing.products:
            prd[i.id] = {'color': i.colors, 'colors': i.colors,
                         'discount': i.discount, 'image': i.image_1, 'name': i.name,
                 'price': float(i.price), 'quantity': i.stock}
            discount = (i.discount / 100) * float(float(i.price))
            subtotal += float(i.price) * int(i.stock)
            subtotal -= discount
            tax = ("%.2f" % (.06 * float(subtotal)))
            grandtotal = float("%.2f" % (1.06 * subtotal))
        cartDisplay['Shoppingcart'] = prd
    else:
        return redirect(url_for('home'))
    # if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
    #     return redirect(url_for('home'))
    # for key, product in session['Shoppingcart'].items():
    #     discount = (product['discount'] / 100) * float(product['price'])
    #     subtotal += float(product['price']) * int(product['quantity'])
    #     subtotal -= discount
    #     tax = ("%.2f" % (.06 * float(subtotal)))
    #     grandtotal = float("%.2f" % (1.06 * subtotal))
    print(cartDisplay)
    stop_timer(resp_time, "getcart")
    return render_template('products/carts.html', tax=tax, grandtotal=grandtotal, brands=brands(),
                           categories=categories(), cart=cartDisplay['Shoppingcart'])


@app.route('/updatecart/<int:code>', methods=['POST'])
@auth_required_buyer
def updatecart(authData, code):
    print(code)
    resp_time = start_timer()
    buyer_data = None
    cartDisplay = {}
    prd ={}
    print(authData)
    if request.method == "POST":
        if authData["isAuthenticated"]:
            buyer_data = authData

        existing = grpc_client.getFromcart(GetCartRequest(customerId=str(buyer_data["userId"])))

        if len(existing.products) == 0:
            return redirect(url_for('home'))

        for i in existing.products:
            prd[i.id] = {'color': i.colors, 'colors': i.colors,
                         'discount': i.discount, 'image': i.image_1, 'name': i.name,
                 'price': float(i.price), 'quantity': i.stock}
        cartDisplay['Shoppingcart'] = prd


        quantity = request.form.get('quantity')
        color = request.form.get('color')

        try:
            session.modified = True
            for key, item in cartDisplay['Shoppingcart'].items():
                if int(key) == code:
                    product = Addproduct.query.filter_by(id=str(key)).first()
                    print(product, quantity)
                    if(int(product.stock) > int(quantity)):
                        grpc_client.updateproductQuantity(UpdateproductQuantity(customer=buyer_data["userId"],
                                                                                product=str(key),
                                                                                quantity=int(quantity)))
                        item['quantity'] = quantity
                        item['color'] = color
                        flash('Item is updated!')
                    else:
                        flash('Requested quantity not present in stock','danger')
                    stop_timer(resp_time, "updatedCart")
                    return redirect(url_for('getCart'))
                else:
                    print("adding")
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))


@app.route('/deleteitem/<int:id>')
@auth_required_buyer
def deleteitem(authData, id):
    resp_time = start_timer()
    cartDisplay = {}
    prd = {}
    if authData["isAuthenticated"]:
        buyer_data = authData

    existing = grpc_client.getFromcart(GetCartRequest(customerId=str(buyer_data["userId"])))

    if len(existing.products) == 0:
        return redirect(url_for('home'))

    for i in existing.products:
        prd[i.id] = {'color': i.colors, 'colors': i.colors,
                     'discount': i.discount, 'image': i.image_1, 'name': i.name,
                     'price': float(i.price), 'quantity': i.stock}
    cartDisplay['Shoppingcart'] = prd

    try:
        session.modified = True
        for key, item in cartDisplay['Shoppingcart'].items():
            if int(key) == id:
                grpc_client.updateproductQuantity(UpdateproductQuantity(customer=buyer_data["userId"],
                                                                        product=str(id), quantity=-99999))
                stop_timer(resp_time, "deleteItem")
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))


@app.route('/clearcart')
@auth_required_buyer
def clearcart(authData):
    try:
        resp_time = start_timer()
        if authData["isAuthenticated"]:
            buyer_data = authData
        print(buyer_data["userId"])
        grpc_client.updateproductQuantity(UpdateproductQuantity(customer=buyer_data["userId"],
                                                                product="387583568568", quantity=0))
        stop_timer(resp_time, "clearcart")
        return redirect(url_for('home'))
    except Exception as e:
        print(e)