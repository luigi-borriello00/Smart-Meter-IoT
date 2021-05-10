# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:52:38 2021

GATEWAY TEST

@author: Luigi
"""

import socket as sk

serverPort = 10000
#uDP
sockClient = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sockClient.bind(("localhost", 10000))
data, address = sockClient.recvfrom(4096)
print(data.decode("utf8"))
message = "KTM"
sockClient.sendto(message.encode(), address)
sockClient.close()

serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
serverSocket.connect(("localhost", serverPort))
serverSocket.send(data)
data = serverSocket.recv(4096)
print(data.decode())
print("ClosingConnection")
serverSocket.close()
