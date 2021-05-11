# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:22:48 2021

@author: Luigi
"""
import time
import socket as sk

def readDetections(client_ip, fileName):
    message = ""
    filePath = "Detections/" + fileName
    file = open(filePath, "r")
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
    return message
    
# Send info to Gatway
def connectToGateway(gateway_address, message):
    # Create the UDP socket
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    buffer = 4096
    try:
        print("Sending info to Gateway on interface 192.168.1.0...")
        time.sleep(2)
        startTime = time.time()
        
        sent = sock.sendto(message.encode(), gateway_address)
        print("Waiting the Gateway response...")
        data, server = sock.recvfrom(buffer)
        # Calculate the time to send the message
        finalTime = time.time() - startTime
        time.sleep(2)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("UDP message's sending time {} and the size of used buffer is {}" .format(finalTime, buffer))
    except Exception as info:
        print(info)
    finally:
        print("Closing Socket")
        sock.close()