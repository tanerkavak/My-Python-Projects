import string
from random import *

character = string.ascii_letters + string.digits + string.punctuation
password_length = int(input("Passport Length: "))

for x in range(0,2):
    password = ""
    for x in range(0,password_length):
        password += "".join(choice(character))

print(password)
input()
