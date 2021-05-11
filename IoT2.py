# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:09:40 2021

@author: Luigi
"""

import IoT_Functions as iotF

# Specific IoT informations
client_ip = "192.168.1.3"
fileName = "DetectionsC2.txt"
gateway_address = ("localhost", 10000)
iotF.readDetections(client_ip, fileName)
iotF.connectToGateway(gateway_address)