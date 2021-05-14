# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:09:40 2021

UDP Device2

@author: Luigi
"""

import IoT_Functions as iotF

# Specific IoT informations
client_ip = "192.168.1.3"
fileName = "DetectionsC2.txt"
gateway_address = ("localhost", 10003)
message = iotF.readDetections(client_ip, fileName)
iotF.connectToGateway(gateway_address, message)
