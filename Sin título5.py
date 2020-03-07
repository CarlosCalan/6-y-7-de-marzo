# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:56:43 2020

@author: CEC
"""

def readint(prompt, min, max):
    while(True):
        try:
            x=int(input(prompt))
            if x >= min and x<=max: #definir maximos y minimos
                return x
                break      
        except ValueError:
            print("Enter a integer value")  
        else:
            print("the value is not within permitted range (min..max)")
        finally:
            print('FIN')            

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)