import string
from random import *

character = string.ascii_uppercase + string.digits

liste = []
key_length = 6
i = 1

while i < key_length:
    password = "".join(choice(character) for x in range(0, key_length))
    liste.append(password)
    i += 1

print(liste[0]+"-"+liste[1]+"-"+liste[2]+"-"+liste[3]+"-"+liste[4]) #Add list index number to print
input()
