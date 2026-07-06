#set is the collection of the unordered items
#each element in the set must be unique and immutable

collection = {1, 2, 2,3, "hello", "world", 3, 4, 5} #repeated elements stored only once , so it resolved to {1, 2}
print(collection)
print(type(collection))
print(len(collection))

collection1 = set()
print(type(collection1))

#Set Methods
collection2 = set()
collection2.add(1)
collection2.add(4)
collection2.add("Aishwarya")
collection2.clear()
print(collection2)
print(len(collection2))

collection3 = {"Hello", "World", "Aishwarya", "coding" "Python"}
print(collection3.pop())
print(collection3.pop())

#union and intersection 
#union = combines both set values and return new 
#intersection = combines common values and return new 

set1 = {1,2,3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1)
print(set2)

set3 = {1,2,3}
set4 = {3,4,5}
print(set3.intersection(set4))