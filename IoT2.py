# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:09:40 2021

@author: Luigi
"""

import socket as sk
import time 

client_ip = "192.168.1.3"

# create the socket
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
gateway_address = ("localhost", 10000)
message = ""
buffer = 4096

# read info from file
file = open("Detections/DetectionsC2.txt", "r")
print("Reading the detections from file...")
time.sleep(2)

while True:
    # Get next line from file
    line = file.readline()
    # formatting the message
    if(line != ""):
        message = message + client_ip + " - " + line + "\n"  
    # if line is empty
    # end of file is reached
    if not line:
        break
    
file.close()
print("Detections readed correctly!")

#Sending the info to the Gateway
try:
    print("Sending info to Gateway on interface 192.168.1.0...")
    time.sleep(2)
    startTime = time.time()
    sent = sock.sendto(message.encode(), gateway_address)
    print("Waiting the Gateway response...")
    data, server = sock.recvfrom(buffer)
    finalTime = time.time() - startTime
    time.sleep(2)
    print("Received Message:" % data.decode("utf8"))
    print("Time of UDP message {0} and the size of used buffer is {1}" .format(finalTime, buffer))
except Exception as info:
    print(info)
finally:
    print("Closing Socket")
    sock.close()
