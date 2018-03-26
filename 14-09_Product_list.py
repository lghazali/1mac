# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    product_list = 1
    index = 0
    while len(list_of_numbers) > index:
        product_list *= list_of_numbers[index]
        index += 1
    return product_list







print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1