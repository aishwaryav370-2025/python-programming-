#WAF that replace all occurrences of "java" with "python" in above file 

with open("practice.txt","r") as f:
    data = f.read()
    data = data.replace("java", "python")
    print(data)
    
    with open("practice.txt", "w") as f:
        f.write(data)
        
#search if the word "learning" exists in the  file or not.

with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("not found")
        
#WAF to find in which line of the file does the word "Learning " occur first.
#print -1 if not found 

def check_for_line():
    word = "Learning"
    data = True
    line_no = 1 
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
    return -1 

print(check_for_line())     

#froma file containing a numbers separted by comma, print the count of even numbers 

with open("practice.txt", "r") as f:
    data =f.read()
    print(data)
    
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(num)
            num = ""
        else:
            num += data[i]