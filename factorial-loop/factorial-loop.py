#!/usr/bin/python3

import sys

# Consts
numberArgsNeeded = 2

# Functions
def factorial(number):
	res = 1
	while number > 0:
		res = res * (number)
		number = number - 1
	return res
	return "Isn't a number"

# Main
if __name__ == "__main__":
	print(factorial(int(sys.argv[1])))
