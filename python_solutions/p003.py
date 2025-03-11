#!/usr/bin/env python3

# Solution to problem 2
## Largest Prime Factor for given number

def main():
    # return larges prime factor
    num = int(input("Number: "))
    factors = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num /= div
        div = div + 1

    return max(factors)
            
if __name__ == "__main__":
	print(main())
