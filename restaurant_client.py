from __future__ import print_function

import logging

import grpc, os
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = restaurant_pb2_grpc.RestaurantStub(channel)
        response = stub.DrinkOrder(restaurant_pb2.RestaurantRequest(orderID="12345abc", items=[ "fizzy drink", "water", "water" ]))
    print("Greeter client received: " + str(response.orderID) + " & " + str(response.status))


if __name__ == '__main__':
    logging.basicConfig()
    run()
