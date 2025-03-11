#!/usr/bin/env python3

# Solution to problem 5
## Smallest Multiple (Evenly divisible by all of the numbers from 1 to 20)

def main():
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
            
         
if __name__ == "__main__":
	print(main())
