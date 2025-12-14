#------------------- set.add --------------------

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("reshma nasreen")
collection.add([1,2,3])

collection.remove(7)  #--------------------- set. remove -----------------------
collection.clear() #-----------------------------set.clear ----------------------------
print(collection)




collection = {"hello","apna college", " world","coding","python"}

print(collection.pop())



#----------------set.union -----------------

set1 ={1,2,3,4}
set2 ={2,3,4,5}

print(set1.union(set2))  #{1,2,3,4}
print(set1)
print(set2)