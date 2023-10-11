import random
import string

password_len = int(input("Write pasword length:"))
my_password = ""

for i in range(password_len):
  my_password += random.choice(string.printable.strip())

print("Your new password:", my_password)