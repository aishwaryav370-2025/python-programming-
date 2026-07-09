#WAP to print the len of the list (list is the parameter)  

cities = ("delhi", "gurgaon", "noida", "pune", "mumbai", "bengaluru")
heroes = ("thor", "yash", " captain america", "shakti man")

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)

#WAF to print the elements of a list in a single line (list is the parameter)

movies = ("toxic", "kgf", "googly", "lucky")
print(movies[0], end=" ")
print(movies[1], end=" ")