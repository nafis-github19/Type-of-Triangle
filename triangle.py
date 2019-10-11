# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 02:50:39 2019

@author: Nafis
"""

side1 = float(input("Enter length for side1: "))
side2 = float(input("Enter length for side2: "))
side3 = float(input("Enter length for side3: "))

if side1 == side2 and side1 == side3 and side2 == side3:
    print("This is an Equilateral Triangle")
    
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an Isosceles Triangle")
    
else:
    print("This is a Triangle with all the sides of random length ")
    