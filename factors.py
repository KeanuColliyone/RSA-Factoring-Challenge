#!/usr/bin/python3
import sys


def factorize_number(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None


def factorize_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        num = int(num)
        factor1, factor2 = factorize_number(num)
        print(f"{num}={factor1}*{factor2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        file_path = sys.argv[1]
        factorize_numbers(file_path)
