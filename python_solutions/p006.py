#!/usr/bin/env python3

# Solution to problem 6
## Sum Square Difference

def main():
    n = int(input("n: "))
    sum_squares = int((n*(n+1)*(2*n+1))/6)
    squares_sum = int(((n*(n+1))/2)**2)
    diff = squares_sum - sum_squares

    return diff   
         
if __name__ == "__main__":
	print(main())
