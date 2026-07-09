#function is the block of statement that performs a specific task 

def calc_sum(a, b): #parameters 
    sum = a + b 
    print(sum)
    return sum 

calc_sum(5, 10) #function calls
calc_sum(10, 20)
calc_sum(2,7)

#average of 3 numbers 

def calc_avg(a, b, c):
    sum = a + b + c 
    avg = sum / 3
    print(avg)
    return avg 

calc_avg(87, 90, 95)
