list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = [1,2,3,4,5]
list4 = [1,2,3,4,5]

def proc(mylist):
   global list1
   list1  = mylist
   #mylist = list1
   print list1
   #print mylist
   list1 = list1 + [6,7]
   mylist = mylist + [6,7]
def proc2(mylist):
   mylist.append(6)
   mylist.append(7)
def proc3(mylist):
   mylist+=[6,7]

print "demonstrating proc"
print list1
proc(list1)
print list1
print "demonstrating proc2"
print list2
proc2(list2)
print list2
print "demonstrating proc3"
print list3
proc2(list3)
print list3
print ' test list + [6,7]'
print list1 + [6,7]
