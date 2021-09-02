#!/usr/bin/python3

import sys

numArgsNeeded = 2

def factorial(number):
	if number > 1:
		number = number*factorial(number-1)
		return number
	else:
		return number

if __name__ == "__main__":
	if len(sys.argv) < numArgsNeeded:
		print("You need more arguments")
	else:
		print(factorial(int(sys.argv[1])))
