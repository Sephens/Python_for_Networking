mlist = ['a', 'b', 'c', 'd', 'e', 'f']

# If you omit the first index, the slice starts at the beginning. If you omit the second, the slice
# goes to the end. So if you omit both, the slice is a copy of the whole list.
print(mlist[:2])
print(mlist[2:])
print(mlist[:])

# List methods
# append - adds an element to the end of the list
mlist.append('g')
print(mlist)

# extend - takes a list as argument and appends all the elements

list2 = ['h', 'i', 'j']
mlist.extend(list2)
print(mlist)

# sort - arranges the elements of a list from low to high
numbers = [10,8,4,7,6,1,2]
numbers.sort()
print(numbers)

# coding the python sum method
def total_sum(t):
    total = 0
    for x in t:
        total += x
    return total

ans = total_sum(numbers)
print(ans)

print(sum(numbers))


def capitalizer(a):
    caps = []
    for i in a:
        caps.append(i.capitalize())
    return caps

my_list = capitalizer(mlist)
print(my_list)

# deleting elememts from a list
# pop modifies the list and returns the element that was removed. If you don’t provide an
# index, it deletes and returns the last element.

popped = mlist.pop(2)
print(popped)
print(mlist)

# If you know the element you want to remove (but not the index), you can use remove:
removed = mlist.remove('i')
print(mlist)

# To remove more than one element, you can use del with a slice index:
del mlist[2:5]
print(mlist)


# Lists and strings
# To convert from a string to a list of characters, you can use list

name = "John"
t = list(name)
print(t)

# The list function breaks a string into individual letters. If you want to break a string into
# words, you can use the split method:

names = "John McAthy Adams"
splitted = names.split()
print(splitted)


# Object and values
# In this example, Python only created one string object, and both a and b refer to it. But
#  when you create two lists, you get two objects:
a = "dog"
b = "dog"

print(a is b) # True

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y) # False

# In this case we would say that the two lists are equivalent, because they have the same elements,
# but not identical, because they are not the same object. If two objects are identical,
# they are also equivalent, but if they are equivalent, they are not necessarily identical.


# Aliasing
# The association of a variable with an object is called a reference. In this example, there are
# two references to the same object.
# An object with more than one reference has more than one name, so we say that the object
# is aliased.

