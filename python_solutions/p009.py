#!/usr/bin/env python3

# Solution to problem 9
## Special Pythagorean Triples (find product for abc)

def main():
    number = int(input("n: "))
    ans = []
    for a in range(1, number):
          for b in range(a+1, number):
                c = number-a-b
                if (a*a+b*b) == (c*c):
                    ans = [a, b, c]

    return ans[0]*ans[1]*ans[2]
        
if __name__ == "__main__":
	print(main())
