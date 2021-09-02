#!/usr/bin/python3

import sys

# Constant
numArgsNeeded = 2

# Functions
def factorial(number):
	if number > 0:
		number = number*factorial(number-1)
	elif number == 0:
		number = 1
	return number
# Main
if __name__ == "__main__":
	if len(sys.argv) < numArgsNeeded:
		print("You need one argument")
		print(">> ./factorial.py <number>")
	else:
		print(factorial(int(sys.argv[1])))
