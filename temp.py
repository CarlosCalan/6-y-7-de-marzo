# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def readint(prompt, min, max):
    
    print (prompt)
    try:
        x=int(input())
        if x<=max and x>=min:
            return x   
    except ValueError:
        print("Enter a integer value")
        v = readint("Enter a number from -10 to 10: ", -10, 10)
   
    else:
        print("the value is not within permitted range (min..max)")
        v = readint("Enter a number from -10 to 10: ", -10, 10)
    

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

