#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("The number must be non-negative.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    result = factorial(num)
    print(result)

if __name__ == "__main__":
    main()
