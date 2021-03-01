import grpc
from onlineshopping_pb2_grpc import BuyerActionsStub
from onlineshopping_pb2 import AccountCreationRequest

channel = grpc.insecure_channel("localhost:50051")
client = BuyerActionsStub(channel)
request = AccountCreationRequest(buyer_id=2, buyer_name="namratha", buyer_username="nmk", buyer_password="password", items_purchased=1)
print(request)
print(client.createAccount(request))