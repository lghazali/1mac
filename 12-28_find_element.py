# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
def find_element(my_list,value):
    i = 0
    for element in my_list:
        if element == value:
            return i
        else: i += 1
    return -1

# A simpler solution using a built in function
def find_element_bi(my_list, value):
    if value in my_list: return my_list.index(value)
    return -1


print find_element([1, 2, 3], 3)
print find_element_bi([1, 2, 3], 3)
#>>> 2

print find_element(['alpha', 'beta'], 'gamma')
print find_element_bi(['alpha', 'beta'], 'gamma')
#>>> -1

p = [1, 2]
q = p
q.append(3)
print p