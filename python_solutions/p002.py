#!/usr/bin/env python3

# Solution to problem 1
## Find the sum of all even numbers in fibonacci sequence below 4_000_000

def fib():
    num = int(input("Max number: "))
    counter = 0
    x = [0, 1]

    while True:
        if x[-1] < num:
             x.append(x[-2] + x[-1])

             if x[-1] % 2 == 0:
                  counter += x[-1]
        else:
             break

    return counter
            
if __name__ == "__main__":
	print(fib())
