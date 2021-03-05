import decimal

import onlineshopping_pb2_grpc
from mapper.object_mapper import ObjectMapper
from datetime import datetime
import random
from bson import json_util
from onlineshopping_pb2 import (
    AccountCreationResponse, AccountCreationRequest, SearchProductResponse, ProductDetails,
    AddToCartResponse, SearchProductRequestByDesc
)
from models import Register, Base, DBSession, engine, Addproduct, cart
import json
from google.protobuf.json_format import Parse

Base.metadata.create_all(engine)
session = DBSession()


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)


class BuyerActionService(onlineshopping_pb2_grpc.BuyerActionsServicer):
    def createAccount(self, request, context):
        try:
            print("hi")
            print(request)
            record = Register(id=request.buyer_id,
                              name=request.buyer_name,
                              username=request.buyer_username,email=request.buyer_email,
                              password=request.buyer_password,country=request.buyer_country,
                              city=request.buyer_city,contact=request.buyer_contact,
                              address=request.buyer_address,zipcode=request.buyer_zipcode,
                              profile='profile.jpg',date_created=datetime.now(),
                              itemspurchased=request.items_purchased)
            session.add(record)
            session.commit()
        except Exception as e:
            print("Exception")
            print(e)
            AccountCreationResponse(status="failure")
        return AccountCreationResponse(status="success")

    # def getAccounts(self, request, context):
    #     try:
    #         list_users = []
    #         query = {'username': { '$exists' : True}}
    #         entries= buyers.find(query)
    #         for entry in entries:
    #             name = AccountCreationRequest\
    #                 (buyer_id=entry['userId'],
    #                  buyer_name=entry['name'],
    #                  buyer_username=entry['username'],
    #                  buyer_password=entry['password'],
    #                  items_purchased=entry['noOfItemsPurchased'])
    #             list_users.append(name)
    #             print(entry)
    #     except Exception as e:
    #         print(e)
    #     return Accounts(accounts=list_users)

    def login(self, request, context):
        try:
            print("hello")
            user = session.query(Register).filter(Register.email == request.buyer_username).first()
            print(user.name)
            if(user.password == request.buyer_password):
                print("hi")
                return AccountCreationRequest\
                (buyer_id=user.id,
                 buyer_name=user.name,
                 buyer_username=user.username,
                 buyer_password=user.password,
                 items_purchased=user.itemspurchased,
                 is_active="true")

        except Exception as e:
            print(e)
        return AccountCreationRequest()

    def search(self, request, context):
        json_docs = []
        print(request)
        product = session.query(Addproduct).filter(Addproduct.id == request.product).first()
        print(product)
        json_docs.append(ProductDetails(
        id = product.id,
        name = product.name,
        price = str(product.price),
        discount = product.discount,
        stock = product.stock,
        colors = product.colors,
        desc = product.desc,
        pub_date = str(product.pub_date),
        category_id = product.category_id,
        category = product.category.name,
        brand_id = product.brand_id,
        brand = product.brand.name,
        image_1 = product.image_1,
        image_2 = product.image_2,
        image_3 = product.image_3,
        condition = product.condition
        ))
        return SearchProductResponse(products=json_docs)

    def addToCart(self, request, context):
        print(request)
        try:
            id = random.randint(0, 10000)
            session.add(cart(id=id, product_id=request.products.products[0].id,
            customer_id = int(request.customerId),
            name = request.products.products[0].name,
            price = str(request.products.products[0].price),
            discount = request.products.products[0].discount,
            stock = 1,
            colors = request.products.products[0].colors,
            desc = request.products.products[0].desc,
            pub_date = str(request.products.products[0].pub_date),
            image_1 = request.products.products[0].image_1,
            image_2 = request.products.products[0].image_2,
            image_3 = request.products.products[0].image_3
            ))
            session.commit()
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
        products = session.query(cart).filter(cart.customer_id == int(request.customerId)).all()
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
            if(request.quantity == -99999):
                products = session.query(cart).filter(cart.customer_id == request.customer
                                                  , cart.product_id == request.product).all()
                for o in products:
                    session.delete(o)
                session.commit()
                return AddToCartResponse(status="success", price="23")

            if(request.quantity == 0):
                products = session.query(cart).filter(cart.customer_id == request.customer).all()
                for o in products:
                    session.delete(o)
                session.commit()
                return AddToCartResponse(status="success", price="23")

            products = session.query(cart).filter(cart.product_id == request.product , cart.customer_id == request.customer).first()
            products.stock = request.quantity
            session.commit()
            return AddToCartResponse(status="success", price="23")
        except Exception as e:
            print(e)
            return AddToCartResponse(status="failure", price="23")




