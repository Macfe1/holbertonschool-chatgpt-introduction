#!/usr/bin/python3
import sys

def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementa n en cada iteración
    return result

def main():
    if len(sys.argv) != 2:
        print("Uso: {} <número>".format(sys.argv[0]))
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: El argumento debe ser un número entero.")
        sys.exit(1)
    
    try:
        f = factorial(number)
        print(f)
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()