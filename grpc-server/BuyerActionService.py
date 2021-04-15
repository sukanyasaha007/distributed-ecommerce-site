import decimal
import socket
import random
import os
import onlineshopping_pb2_grpc
from onlineshopping_pb2 import (
    AccountCreationResponse, AccountCreationRequest, SearchProductResponse, ProductDetails,
    AddToCartResponse
)
from models import Register, Base, DBSession, engine, Addproduct, cart
import json

Base.metadata.create_all(engine)
session = DBSession()

# UDP_IP = "35.224.63.87"
UDP_IP = ["34.68.92.73", "35.193.31.141", "34.122.75.220", "35.197.116.39"]
UPD_PORTS = [5010, 5001, 5002, 5003]
UNHEALTHY_UPD_PORTS = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.settimeout(5.0)


class BuyerActionService(onlineshopping_pb2_grpc.BuyerActionsServicer):

    def __init__(self):
        self.procs_active = None

    def health_check(self):
        UNHEALTHY_UPD_PORTS.clear()
        active_servers = 0
        for ip, port in zip(UDP_IP, UPD_PORTS):
            print("UDP target IP: %s" % ip)
            print("UDP target port: %s" % port)
            hostname = ip
            response = os.system("ping -c 1 " + hostname)
            try:
                if response == 0:
                    print(hostname, 'is up!')
                    active_servers += 1
                else:
                    print(hostname, 'is down!')
                    UNHEALTHY_UPD_PORTS.append(port)
            except Exception as e:
                print(e)
        self.procs_active = active_servers

    def sendToAtomicBroadcastServer(self, request):
        i = 0
        for ip, port in zip(UDP_IP, UPD_PORTS):
            if(port not in UNHEALTHY_UPD_PORTS):
                request["proc_no"] = i
                print("UDP target IP: %s" % ip)
                print("UDP target port: %s" % port)
                print("message: %s" % request)
                i += 1
                try:
                    sock.sendto(json.dumps(request).encode(), (ip, port))
                except Exception as e:
                    print(e)

    def createAccount(self, request, context):
        try:
            self.health_check()
            print("hi")
            print(request)
            request = {"buyer_id": request.buyer_id,
                       "buyer_name": request.buyer_name,
                       "buyer_username": request.buyer_username,
                       "buyer_password": request.buyer_password,
                       "buyer_email": request.buyer_email,
                       "buyer_country": request.buyer_country,
                       "buyer_city": request.buyer_city,
                       "buyer_contact": request.buyer_contact,
                       "buyer_address": request.buyer_address,
                       "buyer_zipcode": request.buyer_zipcode,
                       "items_purchased": request.items_purchased,
                       "type": "client",
                       "function": "createAccount",
                       "procs_active": self.procs_active,
                       }
            self.sendToAtomicBroadcastServer(request)

        except Exception as e:
            print("Exception")
            print(e)
            AccountCreationResponse(status="failure")
        return AccountCreationResponse(status="success")


    def login(self, request, context):
        session.commit()
        # self.health_check()
        try:
            print("hello")
            user = session.query(Register).filter(Register.email == request.buyer_username).first()
            print(user.name)
            if (user.password == request.buyer_password):
                print("hi")
                return AccountCreationRequest \
                    (buyer_id=user.id,
                     buyer_name=user.name,
                     buyer_username=user.username,
                     buyer_password=user.password,
                     items_purchased=user.itemspurchased,
                     is_active="true")
        except Exception as e:
            print(e)
        return AccountCreationRequest()



    # def search(self, request, context):
    #     session.commit()
    #     json_docs = []
    #     print(request)
    #     product = session.query(Addproduct).filter(Addproduct.id == request.product).first()
    #     print(product)
    #     json_docs.append(ProductDetails(
    #     id = product.id,
    #     name = product.name,
    #     price = str(product.price),
    #     discount = product.discount,
    #     stock = product.stock,
    #     colors = product.colors,
    #     desc = product.desc,
    #     pub_date = str(product.pub_date),
    #     category_id = product.category_id,
    #     category = product.category.name,
    #     brand_id = product.brand_id,
    #     brand = product.brand.name,
    #     image_1 = product.image_1,
    #     image_2 = product.image_2,
    #     image_3 = product.image_3,
    #     condition = product.condition
    #     ))
    #     return SearchProductResponse(products=json_docs)

    def addToCart(self, request, context):
        session.commit()
        print(request)
        try:
            id = random.randint(0, 10000)
            request  = {
                "id": id,
                "product_id" : request.products.products[0].id,
                "customer_id" : int(request.customerId),
                "name" : request.products.products[0].name,
                "price" : str(request.products.products[0].price),
                "discount" : request.products.products[0].discount,
                "stock" : 1,
                "colors" : request.products.products[0].colors,
                "desc" : request.products.products[0].desc,
                "image_1": request.products.products[0].image_1,
                "image_2" : request.products.products[0].image_2,
                "image_3" : request.products.products[0].image_3,
                "pub_date" : str(request.products.products[0].pub_date),
                "type": "client",
                "function": "addToCart",
                "procs_active": self.procs_active,
            }
            self.sendToAtomicBroadcastServer(request)
            return AddToCartResponse(status="success", price="23")
        except Exception as e:
            print(e)
            return AddToCartResponse(status="failure", price="56")

        # json_docs = []
        # try:
        #     items = products.find(query)
        #     if(items.count() == 0):
        #         return SearchProductResponse(products=json_docs)
        #     else:
        #         for item in items:
        #             keywords = []
        #             for it in item['keywords']:
        #                 keywords.append(Keyword(words=it))
        #             json_docs.append(ProductDetails(
        #                 productId = item['productId'],
        #                 product_name = item['product_name'],
        #                 price = item['price'],
        #                 quantity = item['quantity'],
        #                 seller_id = item['seller_id'],
        #                 category = item['category'],
        #                 category_name = item['category_name'],
        #                 keywords = keywords
        #             ))
        # except Exception as e:
        #     print(e)
        # return SearchProductResponse(products=json_docs)

    def getProducts(self, request, context):
        json_docs = []
        try:
            items = products.find({"productId": {"$exists": True}})
            for item in items:
                keywords = []
                for it in item['keywords']:
                    keywords.append(Keyword(words=it))
                json_docs.append(ProductDetails(
                    productId=item['productId'],
                    product_name=item['product_name'],
                    price=item['price'],
                    quantity=item['quantity'],
                    seller_id=item['seller_id'],
                    category=item['category'],
                    category_name=item['category_name'],
                    keywords=keywords
                ))
        except Exception as e:
            print(e)
        return SearchProductResponse(products=json_docs)


    def getProductsBySearchword(self, request, context):
        session.commit()
        regex = r'.*' + request.searchword + '.*'
        products = session.query(Addproduct).filter(Addproduct.desc.op('regexp')(regex) |
                                                    Addproduct.name.op('regexp')(regex)).all()
        listProducts = []
        for product in products:
            message = ProductDetails()
            message.id = product.id
            message.name = product.name
            message.price = str(product.price)
            message.discount = product.discount
            message.stock = product.stock
            message.colors = product.colors
            message.desc = product.desc
            message.pub_date = str(product.pub_date)
            message.category_id = product.category_id
            message.category = product.category.name
            message.brand_id = product.brand_id
            message.brand = product.brand.name
            message.image_1 = product.image_1
            message.image_2 = product.image_2
            message.image_3 = product.image_3
            if(product.condition == None):
                message.condition = "new"
            listProducts.append(message)
        searchprodResponse = SearchProductResponse(products=listProducts)
        return searchprodResponse

    def getFromcart(self,  request, context):
        print(request)
        session.commit()
        products = session.query(cart).filter(cart.customer_id == int(request.customerId)).all()
        products1 = session.query(cart).all()
        for pr in products:
            print(pr.name)
        listProducts = []
        for product in products:
            message = ProductDetails()
            message.id = product.product_id
            message.name = product.name
            message.price = str(product.price)
            message.discount = product.discount
            message.stock = product.stock
            message.colors = product.colors
            message.desc = product.descp
            message.pub_date = str(product.pub_date)
            message.category_id = 123
            message.category = "random"
            message.brand_id = 123
            message.brand = "random"
            message.image_1 = product.image_1
            message.image_2 = product.image_2
            message.image_3 = product.image_3
            message.condition = "new"
            listProducts.append(message)

        searchprodResponse = SearchProductResponse(products=listProducts)
        return searchprodResponse

    def updateproductQuantity(self,  request, context):
        try:
            request = {
                "customer" : request.customer,
                "product" : request.product,
                "quantity" : request.quantity,
                "type": "client",
                "function": "updateproductQuantity",
                "procs_active": self.procs_active,
            }
            self.sendToAtomicBroadcastServer(request)
            return AddToCartResponse(status="success", price="23")
        except Exception as e:
            print(e)
            return AddToCartResponse(status="failure", price="23")




