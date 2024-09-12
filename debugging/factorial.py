#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementa el valor de n en cada iteración
    return result

if len(sys.argv) != 2:
    print("Uso: ./factorial.py <número>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    f = factorial(n)
    print(f)
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
