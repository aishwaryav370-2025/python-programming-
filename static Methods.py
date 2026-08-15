#Methods that don't use the self parameter (work at calss level)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks
        
        
    @staticmethod
    def welcome():
        print("Welcome student")
        
    def get_avg(self):
        sum = 0 
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average is:", sum/3)
        
s1 = Student("Aishwarya", [90, 80, 70])
s1.get_avg()
s1.welcome()