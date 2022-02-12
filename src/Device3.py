# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:09:40 2021

UDP Device3

@author: Luigi
"""

import IoT_Functions as iotF

# Specific IoT informations
client_ip = "192.168.1.4"
fileName = "DetectionsC3.txt"
gateway_address = ("localhost", 10003)
message = iotF.readDetections(client_ip, fileName)
iotF.connectToGateway(gateway_address, message)