#!/usr/bin/python3
import sys

def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    """Función principal que maneja la entrada y salida del programa."""
    if len(sys.argv) != 2:
        print("Uso: ./factorial.py <número>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("El número debe ser un entero positivo.")
        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
