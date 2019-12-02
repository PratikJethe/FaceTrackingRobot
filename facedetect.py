# import websocket
#
# # Connect to WebSocket server
# ws = websocket.WebSocket()
# ws.connect("ws://192.168.0.112")
# print("Connected to WebSocket server")
#
# # Ask the user for some input and transmit it
# str = input("Say something: ")
# ws.send(str)
#
# # Wait for server to respond and print it
# result = ws.recv()
# print("Received: " + result)
#
# # Gracefully close WebSocket connection
# ws.close()
#
#
# import socket
#
# s = socket.socket()
#
#
# s.bind(('', 80))
# s.listen(0)
#
# # while True:
# #
# #     client, addr = s.accept()
# #
# #     while True:
# #         content = client.recv(32)
# #
# #         if len(content) == 0:
# #             break
# #
# #         else:
# #             print(content)
# #             client.send("Left".encode())
# #             client.recv(32)
# #
# #     print("Closing connection")
# #     client.close()
#
# client,addr = s.accept()
# while True:
#     data = client.recv(32)
#     print(data)
#     print()
#     client.send("test".encode('utf-8'))
#     #idata = input("ENTER THE REPLY>>>")
#
#     #if(idata!="close"):
#     client.send("hello".encode('utf-8'))
#
#     # else:
#     #     client.send(idata.encode('utf-8'))
#     #     client.close()
#     #     client.close()
#     #     break
# print("closing")
import requests
import time
n=0
def makeurl(direction):
    url =  "http://192.168.0.112/"+direction
    try:
        requests.get(url)
    except:
        print("OK")
while (n<6):
    print("LEFT SENDING")
    makeurl("left")
    # print("RIGHT SENDING")
    # makeurl("right")
    # print("CENTER SENDING")
    # makeurl("center")
    # print("SEARCH SENDING")
    # makeurl("search")

