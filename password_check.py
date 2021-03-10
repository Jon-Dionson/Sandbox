MIN_LENGTH = 3
MAX_LENGTH = 10
password = input("Enter a password: ")

while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
    print("Invalid Password")
    password = input("Enter a password: ")
print(len(password) * "*")
