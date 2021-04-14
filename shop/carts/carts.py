from flask import render_template, session, request, redirect, url_for, flash, current_app
from shop import db, app, start_timer, stop_timer
from shop.products.routes import brands, categories
from flask_login import current_user
from shop.grpc_server.onlineshopping_pb2 import SearchProductRequest, AddToCartRequest, UpdateproductQuantity, GetCartRequest
from shop.products.models import cart
from shop import grpc_client


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))


@app.route('/addcart', methods=['POST'])
def AddCart():
    try:
        resp_time = start_timer()
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        print(product_id)
        item = SearchProductRequest(product=product_id)
        response = grpc_client.search(item)
        product = response.products
        if request.method == "POST":
            DictItems = {
                product_id: {'name': product[0].name, 'price': float(product[0].price), 'discount': product[0].discount,
                             'color': color, 'quantity': quantity, 'image': product[0].image_1,
                             'colors': product[0].colors}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            grpc_client.updateproductQuantity(UpdateproductQuantity(customer=current_user.id,
                                                              product=str(product_id),
                                                                                    quantity=int(item['quantity'])+1))
                            session.modified = True
                            item['quantity'] += 1
                else:
                    session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    grpc_client.addToCart(AddToCartRequest(customerId=str(current_user.id), products=response))
                    return redirect(request.referrer)
            else:
                res = grpc_client.addToCart(AddToCartRequest(customerId=str(current_user.id), products=response))
                print(res.status)
                session['Shoppingcart'] = DictItems
                stop_timer(resp_time, "addTocart")
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/carts')
def getCart():
    resp_time = start_timer()
    existing = grpc_client.getFromcart(GetCartRequest(customerId=str(current_user.id)))
    print("cart contents -> ", existing)
    prd = {}
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
        session['Shoppingcart'] = prd
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
    stop_timer(resp_time, "getcart")
    return render_template('products/carts.html', tax=tax, grandtotal=grandtotal, brands=brands(),
                           categories=categories())


@app.route('/updatecart/<int:code>', methods=['POST'])
def updatecart(code):
    resp_time = start_timer()
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        color = request.form.get('color')
        try:
            session.modified = True
            for key, item in session['Shoppingcart'].items():
                if int(key) == code:
                    detail = SearchProductRequest(product=str(key))
                    response = grpc_client.search(detail)
                    product = response.products
                    print(product, quantity)
                    if(int(product[0].stock) > int(quantity)):
                        grpc_client.updateproductQuantity(UpdateproductQuantity(customer=current_user.id,
                                                                                product=str(key),
                                                                                quantity=int(quantity)))
                        item['quantity'] = quantity
                        item['color'] = color
                        flash('Item is updated!')
                    else:
                        flash('Requested quantity not present in stock','danger')
                    stop_timer(resp_time, "updatedCart")
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))


@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    resp_time = start_timer()
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key, item in session['Shoppingcart'].items():
            if int(key) == id:
                grpc_client.updateproductQuantity(UpdateproductQuantity(customer=current_user.id,
                                                                        product=str(id), quantity=-99999))
                session['Shoppingcart'].pop(key, None)
                stop_timer(resp_time, "deleteItem")
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))


@app.route('/clearcart')
def clearcart():
    try:
        resp_time = start_timer()
        print(current_user.id)
        grpc_client.updateproductQuantity(UpdateproductQuantity(customer=current_user.id,
                                                                product="387583568568", quantity=0))
        stop_timer(resp_time, "clearcart")
        session.pop('Shoppingcart', None)
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
