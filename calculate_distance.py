import math

def calDistance(x1,y1,x2,y2):
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))


print calDistance(1, 0, 0, 0)
#1.0
print calDistance(1, 1, 1, 1)
#0.0
print calDistance(0, 0, 1, 1)
#1.4142135623730951
