import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXY"
lower = "abcdefghijklmnopqrstuvwxyz"
symbol = "@!#$%^&*:"
all = lower + upper + symbol
len = 8
password ="".join(random.sample(all, len))
print(password)
