#Tuples in python is a built in data type that lets us create immutable sequences of values
#immutable just like strings 

tuple = (1, 2, 4, 5, 6, 7, 9,)
print(tuple[0])
print(tuple[2])
print(tuple[1:4])

tup = (1,)
print(tup)
print(type(tup))

#Tuple Methods
tup2 = (1, 3, 5, 1)
print(tup2.index(3))
print(tup2.count(1))