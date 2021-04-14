import json
from datetime import datetime
import random
from models import Register, cart
from onlineshopping_pb2 import AccountCreationRequest


class dbops():

    def createAccount(request, session):
        request = json.loads(request)
        record = Register(id=request["buyer_id"],
                          name=request["buyer_name"],
                          username=request["buyer_username"], email=request["buyer_email"],
                          password=request["buyer_password"], country=request["buyer_country"],
                          city=request["buyer_city"], contact=request["buyer_contact"],
                          address=request["buyer_address"], zipcode=request["buyer_zipcode"],
                          profile='profile.jpg', date_created=datetime.now(),
                          itemspurchased=request["items_purchased"])
        session.add(record)
        session.commit()

    def login(request, session, sock):
        try:
            print("hello")
            request = json.loads(request)
            print(request)
            user = session.query(Register).filter(Register.email == request["buyer_username"]).first()
            print(user.password)
            print(request["buyer_password"])
            if(user.password == request["buyer_password"]):
                print("hi")
                # return AccountCreationRequest\
                # (buyer_id=user.id,
                #  buyer_name=user.name,
                #  buyer_username=user.username,
                #  buyer_password=user.password,
                #  items_purchased=user.itemspurchased,
                #  is_active="true")
                sock.sendto(json.dumps({
                    "buyer_id" : user.id,
                    "buyer_name": user.name,
                    "buyer_username": user.username,
                    "buyer_password": user.password,
                    "items_purchased": user.itemspurchased,
                    "is_active": "true"}).encode(), ("127.0.0.1", 5005))
            else:
                sock.sendto(json.dumps({
                    "failure": "yes",
                    "is_active": "true"}).encode(), ("127.0.0.1", 5005))


        except Exception as e:
            print(e)
            sock.sendto(json.dumps({
                "failure": "yes",
                "is_active": "true"}).encode(), ("127.0.0.1", 5005))

    def addToCart(request, session):
        print("adding to cart")

        request = json.loads(request)
        try:
            id = random.randint(0, 10000)
            session.add(cart(id=id, product_id=request["product_id"],
            customer_id = int(request["customer_id"]),
            name = request["name"],
            price = str(request["price"]),
            discount = request["discount"],
            stock = 1,
            colors = request["colors"],
            desc = request["desc"],
            pub_date = str(request["pub_date"]),
            image_1 = request["image_1"],
            image_2 = request["image_2"],
            image_3 = request["image_3"]
            ))
            session.commit()
        except Exception as e:
            print(e)

    def updateproductQuantity(request, session):
        request = json.loads(request)
        print("deleteing requests")
        try:
            if (request["quantity"] == -99999):
                products = session.query(cart).filter(cart.customer_id == request["customer"]
                                                      , cart.product_id == request["product"]).all()
                for o in products:
                    session.delete(o)
                session.commit()

            elif (request["quantity"] == 0):
                products = session.query(cart).filter(cart.customer_id == request["customer"]).all()
                for o in products:
                    session.delete(o)
                session.commit()

            else:
                products = session.query(cart).filter(cart.product_id == request["product"],
                                                      cart.customer_id == request["customer"]).first()
                products.stock = request["quantity"]
                session.commit()
        except Exception as e:
            print(e)
