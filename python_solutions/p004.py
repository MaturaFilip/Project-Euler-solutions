#!/usr/bin/env python3
from itertools import combinations

# Solution to problem 4
## Largest Palindrome Product

def main():
    # generate pairs
    minimum = int(input("Min number: "))
    maximum = int(input("Max number: "))

    numbers = list(range(minimum, maximum+1))
    pairs = list(combinations(numbers, 2))
    
    # calculate larges palindrome product
    largest = []
    for i in pairs:
        x = str(i[0] * i[1])
          
        if is_palindrome(x):
             largest.append(int(x))

    return max(largest)

# Is string palindrome or not?
def is_palindrome(x):
    x_len = len(x)
    for i in range(0, x_len // 2):
        if (x[i] != x[x_len - i - 1]):
            return False
    return True
         
if __name__ == "__main__":
	print(main())
