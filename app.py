#!/usr/bin/env python3
"""Simple calculator app with a bug"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(f"10 / 2 = {divide(10, 2)}")  # Should print 5, prints 20
