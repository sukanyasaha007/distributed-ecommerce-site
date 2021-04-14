# recommendations/buyerActions.py
from concurrent import futures
import grpc
import logging

import onlineshopping_pb2_grpc
from BuyerActionService import BuyerActionService

# _PORT = os.environ["PORT"]
_PORT = 50051

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    onlineshopping_pb2_grpc.add_BuyerActionsServicer_to_server(
        BuyerActionService(), server
    )
    server.add_insecure_port(f"[::]:{_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()