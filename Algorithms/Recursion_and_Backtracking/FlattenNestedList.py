# A nested list can be traversed and flattened using a recursive function. 
# The base case evaluates an element in the list. 
# If it is not another list, the single element is appended to a flat list. 
# The recursive step calls the recursive function with the nested list element as input.

def flatten(arr):
    result = []
    for i in arr:
        if type(i) == list:
            result += flatten(i)
        else:
            result += i
    return result

print(flatten(['a', ['b', ['c', ['d']], 'e'], 'f']))
# returns ['a', 'b', 'c', 'd', 'e', 'f']