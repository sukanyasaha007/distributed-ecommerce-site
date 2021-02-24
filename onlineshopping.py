# recommendations/buyerActions.py
from datetime import datetime
from concurrent import futures
import random
from sqlalchemy.orm import sessionmaker
from flask_login import login_required, current_user, logout_user, login_user
from sqlalchemy import create_engine
import grpc
import sqlite3

from shop import bcrypt
from shop.grpc_ecommerce.protobufs import onlineshopping_pb2_grpc
from shop.grpc_ecommerce.protobufs.onlineshopping_pb2 import (
    AccountCreationResponse,Accounts, AccountCreationRequest, AccountLoginRequest,
    SearchProductRequest, SearchProductResponse, ProductDetails, Keyword
)
# from shop import bcrypt
from shop.customers.forms import CustomerRegisterForm
from shop.customers.model import Register
from shop.products.models import Addproduct

engine = create_engine('sqlite:///shop/shop.db')
Register.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class BuyerActionService(onlineshopping_pb2_grpc.BuyerActionsServicer):
    def createAccount(self, request, context):
        try:
            print("hi")
            print(request)
            record = Register(id=request.buyer_id, name=request.buyer_name,
                              username=request.buyer_username,email=request.buyer_email,
                              password=request.buyer_password,country=request.buyer_country,
                              city=request.buyer_city,contact=request.buyer_contact,
                              address=request.buyer_address,zipcode=request.buyer_zipcode,
                              profile='profile.jpg',date_created=datetime.now(),
                              itemspurchased=request.items_purchased)
            session.add(record)
            session.commit()
        except Exception as e:
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
            user = Register.query.filter_by(email=request.buyer_username).first()
            print(user.name)
            if(user and bcrypt.check_password_hash(user.password, request.buyer_password)):
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
        products = Addproduct.query.msearch(request.product, fields=['keywords', 'desc'], limit=6)
        for product in products:
            print(product)
            keywords = []
            keywords.append(Keyword(words=product.keywords))
            json_docs.append(ProductDetails(
                productId = product.id,
                product_name = product.name,
                price = product.price,
                quantity = product.stock,
                seller_id = product['seller_id'],
                category = product['category'],
                category_name = product['category_name'],
                keywords = keywords
            ))
        return SearchProductResponse(products=json_docs)
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




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    onlineshopping_pb2_grpc.add_BuyerActionsServicer_to_server(
        BuyerActionService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()