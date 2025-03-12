#!/usr/bin/env python3
import sympy
# Solution to problem 7
## Find 10 001 th prime

def main():
    get_index = int(input("index: "))
    primes = []
    number = 2

    if get_index <= 0:
        return []

    while len(primes) < get_index:
        if sympy.isprime(number):
            primes.append(number)
        number += 1

    return primes[-1]                
         
if __name__ == "__main__":
	print(main())
