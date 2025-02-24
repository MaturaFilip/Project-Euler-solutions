#!/usr/bin/env python3

# Solution to problem 1
## Find the sum of all the multiples of 3 or 5 below 1000

def multiples():
	print("Choose number and I show you the sum of multiples 3 or 5 bellow your number")
	print("")
	num = int(input("Your number: "))
	
	sum = 0
	for i in range(num):
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	print(f"The result is number: {sum:1,d}")

if __name__ == "__main__":
	multiples()
