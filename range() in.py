seq = range(10)

for i in seq:
    print(i)
    
for i in range(10): #range(stop)
    print(i)
    
 # start, stop, step    
for i in range(2, 10, 2): 
    print(i)
    
for i in range(1, 100, 2):
    print(i)
    
for i in range(1,101 ):
    print(i)
    
for i in range(100, 0, -1):
    print(i)
    
n = int(input("enter number: "))

for i in range(1, 11):
    print(n *i)
    
#pass statement-used as place holder 
for i in range(5):
    pass
print("some useful work")