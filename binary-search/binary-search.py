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
		dataList.sort()
		return dataList
	except:
		return "Fail opening file"

def binarySearch(data, sortedList):
	try:
		start = 0
		end = len(sortedList)
		while start != end:
			middle = start + (end - start) // 2
			if sortedList[middle] > str(data):
				end = middle
			elif sortedList[middle] < str(data):
				start = middle + 1
			else:
				return middle
		return "No exist"
	except ZeroDivisionError:
		return "Fail searching data"

# Main
if __name__ == "__main__":
	if len(sys.argv) < numberArgNeeded:
		print("You need put the number you want to search")
		print(">> ./binary-search.py <numberToSearch>")
	else:
		dataToSearch = int(sys.argv[1])
		dataList = readData(FILE)
		position = binarySearch(dataToSearch, dataList)

		if str(position).isnumeric():
			print(str(position) + ": " + dataList[position])
		else:
			print(position)
