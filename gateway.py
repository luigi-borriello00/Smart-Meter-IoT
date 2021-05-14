# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:04:01 2021

Gateway

@author: emanuele.orlietti
"""

import socket as sk
import time

message = ""

socket_device = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
socket_device.bind(("localhost",10003))
print('Listening on the device interface')

# Waiting devices's detections
for i in range(4):
    data, address = socket_device.recvfrom(4096)
    print(address)
    message = message + data.decode("utf8") + '\n'
    time.sleep(2)
    messageReply = "Detection arrived"
    socket_device.sendto(messageReply.encode(), address)
    
socket_device.close()
print("Detections arrived. Open connection interface 10.10.10.0")

# Device detections have arrived and sending everything to the cloud
socket_cloud = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
socket_cloud.connect(('localhost', 8002))
startTime = time.time()
socket_cloud.send(message.encode())
buffer = 4096
data = socket_cloud.recv(buffer)
print("Waiting the server's response...")
finalTime = startTime - time.time()
print("Received Message: {}" .format(data.decode("utf8")))
print("TCP message's sending time {} and the size of used buffer is {}" .format(finalTime, buffer))
print("Closing connection")
socket_cloud.close()
    
