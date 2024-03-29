import seller_pb2_grpc
from datetime import datetime
from seller_pb2 import (
    SellerAddProductsRequest,SellerAddProductsResponse
    # AccountCreationResponse, AccountCreationRequest, SearchProductResponse, ProductDetails, AddToCartResponse
)
from models import Base, DBSession, engine, Addproduct

# from ..shop.products.models import SoldProducts

# from ..shop.customers.model import Register, Rating

# Base.metadata.create_all('mysql+pymysql://root:@localhost/onlineshopping')
Base.metadata.create_all(engine)

session = DBSession()

class SellerActionService(seller_pb2_grpc.SellerServicer):
    def SellerAddProductsRequest(self):
        pass

#     def createAccount(self, request, context):
#         try:
#             print("BuyerActionService.createAccount")
#             print(request)
#             record = Register(id=request.buyer_id,
#                               name=request.buyer_name,
#                               username=request.buyer_username,email=request.buyer_email,
#                               password=request.buyer_password,country=request.buyer_country,
#                               city=request.buyer_city,contact=request.buyer_contact,
#                               address=request.buyer_address,zipcode=request.buyer_zipcode,
#                               profile='profile.jpg',date_created=datetime.now(),
#                               itemspurchased=request.items_purchased)
#             session.add(record)
#             print("DB commited inside")
#             session.commit()
#         except Exception as e:
#             print("Exception")
#             print(e)
#             AccountCreationResponse(status="failure")
#         return AccountCreationResponse(status="success")

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

    # def login(self, request, context):
    #     try:
    #         print("hello")
    #         user = session.query(Register).filter(Register.email == request.buyer_username).first()
    #         print(user.name)
    #         if(user.password == request.buyer_password):
    #             print("hi")
    #             return AccountCreationRequest\
    #             (buyer_id=user.id,
    #              buyer_name=user.name,
    #              buyer_username=user.username,
    #              buyer_password=user.password,
    #              items_purchased=user.itemspurchased,
    #              is_active="true")

    #     except Exception as e:
    #         print(e)
    #     return AccountCreationRequest()

    # def search(self, request, context):
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

    # def addToCart(self, request, context):
    #     print(request)
    #     try:
    #         session.add(cart(product_id=request.products.products[0].id,
    #         customer_id = int(request.customerId),
    #         name = request.products.products[0].name,
    #         price = str(request.products.products[0].price),
    #         discount = request.products.products[0].discount,
    #         stock = 1,
    #         colors = request.products.products[0].colors,
    #         desc = request.products.products[0].desc,
    #         pub_date = str(request.products.products[0].pub_date),
    #         image_1 = request.products.products[0].image_1,
    #         image_2 = request.products.products[0].image_2,
    #         image_3 = request.products.products[0].image_3
    #         ))
    #         session.commit()
    #         return AddToCartResponse(status="success", price="23")
    #     except Exception as e:
    #         return AddToCartResponse(status="failure", price="56")



