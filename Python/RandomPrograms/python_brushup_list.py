# brush up all list methods 
# Note: Lists Store References, Not Values
list = [10, 20, "GfG", 40, True]
# acces  using indexing
print(list[2])
# Checking types of elements
print(type(list[2]) , type(list[1]))


# Adding Elements into List
# We can add elements to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.
# Updating Elements into List
list.append(8)
print(list)
list.extend(['mon',3])
print(list)
list.insert(0,"s")
print(list)
list[1]=100
print(list)

# Removing Elements from List
# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.
del list[4]
print(list)
list.remove('mon')
print(list)
list.pop()
print(list.pop(),list)

for item in list:
    print(item)
    
# Nested Lists in Python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])

# List Comprehension in Python
squres = [x**2 for x in range(1,5)]
print(squres)
