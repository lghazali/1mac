# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.
def measure_udacity (list):
    count = 0
    for element in list:
        if element[0] == 'U': # also can use: if element.find("U") == 0:
            count += 1
    return count




print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
