######################################################################################################################
# Name: Brandon Fortes
# Date: December 12, 2023
# Description: A program that preforms several different sorting algorithms on a list and then displays the number of comparisons and swaps each method did
######################################################################################################################

# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12] 
	# return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
	# return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
	# return [2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
	# return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
	

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(list):
	comparisons = 0
	swaps = 0
	for i in range(1, len(list)): 
		for j in range(0, len(list) - i):
			if (list[j] > list[j + 1]):
				temp = list[j]
				list[j] = list[j + 1]
				list[j + 1] = temp
				swaps += 1
			comparisons += 1
	return list, comparisons, swaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimizedBubbleSort(list):
	comparisons = 0
	swaps = 0
	swapsCheck = 0
	for i in range(1, len(list)): 
		swapsCheck = swaps
		for j in range(0, len(list) - i):
			if (list[j] > list[j + 1]):
				temp = list[j]
				list[j] = list[j + 1]
				list[j + 1] = temp
				swaps += 1
			comparisons += 1
		if (swapsCheck == swaps):
			break
	return list, comparisons, swaps


# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(list):
	comparisons = 0
	swaps = 0
	minIndex = 0
	for i in range(0, len(list) - 1): 
		minIndex = i
		for j in range(i + 1, len(list)):
			if (list[minIndex] > list[j]):
				minIndex = j
			comparisons += 1
		temp = list[minIndex]
		list[minIndex] = list[i]
		list[i] = temp
		swaps += 1
	return list, comparisons, swaps


# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(list):
	newList = [list[0]]
	comparisons = 0
	swaps = 0
	for i in range(1, len(list)):
		newList.append(list[i])
		j = i
		comparisons += 1
		if (newList[j] < newList[j - 1]):
			while (j > 0):
				comparisons += 1
				if (newList[j] < newList[j - 1]):
					temp = newList[j - 1]
					newList[j - 1] = newList[j]
					newList[j] = temp
					swaps += 1
					j -= 1
				else:
					break
		if (j == 0):
			comparisons += 1
	return newList, comparisons, swaps


# the main part of the program
result, comparisons, swaps = bubbleSort(getList())
print(f"The list: {getList()}") 
print(f"After bubble sort: {result}")
print(f"{comparisons} comparisons; {swaps} swaps \n")

result, comparisons, swaps = optimizedBubbleSort(getList())
print(f"The list: {getList()}") 
print(f"After optimized bubble sort: {result}")
print(f"{comparisons} comparisons; {swaps} swaps \n")

result, comparisons, swaps = selectionSort(getList())
print(f"The list: {getList()}") 
print(f"After selection sort: {result}")
print(f"{comparisons} comparisons; {swaps} swaps \n")

result, comparisons, swaps = insertionSort(getList())
print(f"The list: {getList()}") 
print(f"After insertion sort: {result}")
print(f"{comparisons} comparisons; {swaps} swaps \n")



