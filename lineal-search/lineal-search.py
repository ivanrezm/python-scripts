#!/usr/bin/python3

import sys

# Constant
FILE = "IN.txt"
numberArgNeeded = 2

# Functions
def readData(name):
	try:
		dataList = []
		with open(name, "r") as file:
			data = file.read()
		dataList = data.split()
		return dataList
	except:
		return "Fail opening file"

def linealSearch(data, List):
	try:
		position = 0
		for element in List:
			if element == data:
				return position
			position = position + 1
		return "No exist"
	except:
		return "Fail searching data"

# Main
if __name__ == "__main__":
	if len(sys.argv) < numberArgNeeded:
		print("You need put the number you want to search")
		print(">> ./lineal-search.py <numberToSearch>")
	else:
		dataToSearch = sys.argv[1]
		dataList = readData(FILE)
		position = linealSearch(dataToSearch, dataList)

		if str(position).isnumeric():
			print(str(position) + ": " + dataList[position])
		else:
			print(position)
