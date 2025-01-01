# 1. Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists.

def nested_sum(nested_list):
    b = []
    s = 0
    # break down the nested list
    for e in nested_list:
        b.extend(e)
    # loop into the newly created list and sum its elements\
    for i in b:
        s += i
    return s
ans = nested_sum([[1,2,4], [10,20], [40,2,1]])
print(ans)


# 2. Write a function called cumsum that takes a list of numbers and returns the cumulative
# sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list.

def cumsum(nlist):
    total = 0
    result = []
    for n in nlist:
        total = total + n
        result.append(total)
        
    return result
suma = cumsum([1,2,3])
print(suma)

# 3. Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements.

def middle(lst):
    first = []
    last = []
    newlst = []
    for n in lst:
        first = lst[1]
        last = lst[-2]
    newlst.append(first)
    newlst.append(last)
    return newlst

m = middle([1,2,3,4,5,6,7])
print(m)

# 4. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None.

def chop(lst):
