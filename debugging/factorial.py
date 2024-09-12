#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result