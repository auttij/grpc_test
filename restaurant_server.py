import grpc
import sys, os
from concurrent import futures
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]

class Restaurant(restaurant_pb2_grpc.RestaurantServicer):
    def returnResponse(self, found, orderID):
        status = "REJECTED"
        if found:
            status = "ACCEPTED"
        return restaurant_pb2.RestaurantResponse(orderID = orderID, status = status)

    def FoodOrder(self, request, context):
        found = all([i in RESTAURANT_ITEMS_FOOD for i in request.items])
        return self.returnResponse(found, request.orderID)

    def DrinkOrder(self, request, context):
        found = all([i in RESTAURANT_ITEMS_DRINK for i in request.items])
        return self.returnResponse(found, request.orderID)

    def DessertOrder(self, request, context):
        found = all([i in RESTAURANT_ITEMS_DESSERT for i in request.items])
        return self.returnResponse(found, request.orderID)

def serve(port):
    print(f"starting server at port {port}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    n = len(sys.argv)
    if n > 1:
        serve(sys.argv[1])
    else:
        serve("50051")
