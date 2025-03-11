#!/usr/bin/env python3
import math
# Solution to problem 5
## Smallest Multiple (Evenly divisible by all of the numbers from 1 to 20)

def main():
    # brute force solution
    number = 1
    div = 0

    while True:
        for i in range(20, 0, -1):
            if number % i == 0:
                div += 1
                continue
            else:
                div = 0
                break
        if div == 20:
             return number
        else:
             number += 1

        # least common multiples -> faster
        multiples = range(1, 20+1)
        # unpacking operator (splat) -> instead of (1,2,3,4,5...) -> *multiples
        com = math.lcm(*multiples)
            
         
if __name__ == "__main__":
	print(main())
