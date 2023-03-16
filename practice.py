#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:35:47 2023

@author: osfoce
"""

##this is for practice
for x in "banana":
    print(x)
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

if "Free" not in txt:
    print("No, Free is not present")   # Because itd case sensitive

a = "Hello, World!"
b = a.split(",")# for splitting a string
print(b)

age = 27
xy = 'My name is Osfoce, I am {}'
print(xy.format(age))# format concatenate srting and integer

# using an escape character \'
#eg = "We are the so-called "Vikings" from the north"  this gives an error
eg = "We are the so-called \"Vikings\" from the north"
print(eg)

# isinstance is used to check if an object is of a certain type
#eg;
s = 200
print(isinstance(s, int))