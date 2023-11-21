#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")
    name="programmer"
   
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    

def add(num1, num2):
    return num1 + num2

result = add(4, 13) 
print(result)

def halve(number):
     return number / 2

result = halve(72)
print(result)