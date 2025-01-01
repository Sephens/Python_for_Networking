# 1. Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists.

def nested_sum(nested_list):
    b = []
    s = 0
    # break down the nested list
    for e in nested_list:
        b.extend(e)
    # loop into the newly created list and sum its elements
        s += i
    return s
ans = nested_sum([[1,2,4], [10,20], [40,2,1]])
print(ans)

