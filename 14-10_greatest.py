# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    great = 0
    # index = 0
    # while index < len(list_of_numbers):
    #     if list_of_numbers[index] > great:
    #         great = list_of_numbers[index]
    #     index += 1
    if len(list_of_numbers) > 0:
        great = max(list_of_numbers)
    else: great = 0
    return great




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
