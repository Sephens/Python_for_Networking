list = ['a', 'b', 'c', 'd', 'e', 'f']

# If you omit the first index, the slice starts at the beginning. If you omit the second, the slice
# goes to the end. So if you omit both, the slice is a copy of the whole list.
print(list[:2])
print(list[2:])
print(list[:])

# List methods
# append - adds an element to the end of the list
list.append('g')
print(list)