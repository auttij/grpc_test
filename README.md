## Introduction
The code in this repo is part of an assignment for the Aalto-university course CS-E4190 - Cloud Software and Systems

The goal of the assignment was to get familiar with [gRPC](gRPC.io)

The task was to create a gRPC server that functions as a restaurant.Requests with an order ID and a list of items will be sent to the server and it will respond with the order ID and a **ACCEPTED** or **REJECTED** status


## Code structure

The files in application are as follows:
- restaurant.proto contains the message definitions and the following service definition:
  - FoodOrder which will only receive orders that contain food items.
  - DrinkOrder which will only receive orders that contain drink items.
  - DessertOrder which will only receive orders that contain dessert items.
- restaurant_pb2.py generated automatically from restaurant.proto.
- restaurant_pb2_grpc.py generated automatically from restaurant.proto.
- restaurant_server.py which contains the logic of the server backend.
- restaurant_client.py very simple test script, for sending a message to the server

To run the application, you need python.
First install the requirements:
```
pip install -r requirements.txt
```

Start the server backend with:
```
python restaurant_server.py <port>
```
if no port is provided, the application uses the default port 50051

Send message to the server in another shell with:
```
python restaurant_client.py
```
