message = input("Enter a message: ")

secret = ""

for letter in message:
    secret += chr(ord(letter) + 3)

print("Secret message:", secret)