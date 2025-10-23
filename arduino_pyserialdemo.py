# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 11:36:30 2025

@author: jgmor
"""

import serial
import time


ser = serial.Serial('COM5',9600, timeout=1)

time.sleep(2)


def sendString(command):
    ser.write(command.encode())
    time.sleep(0.1)
    
    while ser.in_waiting:
        response = ser.readline().decode().strip()
        print(f"Arduino says: {response}")
        
try:
    while True:
        user_input = input("Enter '1' to turn LED ON, '0' to turn LED OFF, or 'q' to quit: ")
        
        if user_input == '1':
            sendString('1')
        elif user_input == '0':
            sendString('0')
        elif user_input == 'q':
            print("Exiting.")
            break
        else:
            print("Invalid command.")
            
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    ser.close()
