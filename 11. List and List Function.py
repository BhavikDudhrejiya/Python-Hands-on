#LIST IN MUTABLE

#Creating grocery list
grocry = ['Harpic', 'Vim Bar', 'Deodrant', 'Bhindi', 'Lollypop', 100]
print(grocry)

#Accessing list through index: Selecting Deidrant
print(grocry[2])

#Creating numbers list and printing an output
numbers = [2,7,9,11,3]
print(numbers)

#Selecting 7 number through list slicing
print(numbers[2])

#Sorting list
numbers.sort()
print(numbers)

#Sorting list reverse
numbers.reverse()
print(numbers)

#Removing number 9 from the list
numbers.remove(9)
print(numbers)

#Removing last number of the list
numbers.pop()
print(numbers)

#Adding number in the list
numbers.append(9)
print(numbers)

#Adding 100 numbers between 11 and 7 numbers in the list
numbers.insert(1,100)
print(numbers)

#Editing any number through index access
numbers[1] = 98
print(numbers)

#List Methods
'''
append(): Add single element in a list
extend(): Add multiple elements in a list
insert(): Add element in between a list
remove(): Remove elements from list
pop(): Remove last elements from list
clear(): Remove all the elements from list
index(): 
count():
sort():
reverse():
copy():
'''
