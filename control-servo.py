#!/usr/bin/env python3
import serial
import time

time_out = time.time() + 20 

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        num = 1        
        ser.write(str(num).encode('utf-8'))
        
        if time.time() > time_out: # exit while loop after 20 seconds
            break
        
        time.sleep(4)