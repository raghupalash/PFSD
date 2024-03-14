import string
from random import choice

S = string.ascii_letters + string.digits + string.punctuation

l = int(input("Length of the password: "))

password = ""

for _ in range(l):
    c = choice(S)
    password += c

print("Your password is: ", password)
