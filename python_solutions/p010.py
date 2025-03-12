#!/usr/bin/env python3
import sympy
# Solution to problem 10
## Summation of Primes. Find primes below n and return sum

def main():
    treshold = int(input("treshold: "))
    primes = []
    number = 2

    if treshold <= 0:
        return []

    while number < treshold:
        if sympy.isprime(number):
            primes.append(number)
        number += 1

    return sum(primes)              
         
if __name__ == "__main__":
	print(main())
