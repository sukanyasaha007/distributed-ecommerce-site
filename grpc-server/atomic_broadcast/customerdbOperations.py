from models import Register, Base
from datetime import datetime
import json


class dbops():

    def createAccount(request, session):
        request = json.loads(request)
        # request = {"buyer_id":738 , "buyer_name":"sharu", "buyer_username": "sharu", "buyer_password": "1234",
        #            "buyer_email": "sharu@gmail.com",
        # "buyer_country": "india",
        #            "buyer_city": "bangalore", "buyer_contact": "194719", "buyer_address":
        #                "hfqifh", "buyer_zipcode": "848168", "items_purchased":0}
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
