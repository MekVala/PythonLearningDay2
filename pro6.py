# Email id matching Using
import re

email = input("Enter Email: ")

match = re.match(r'[a-zA-Z0-9]+@[a-zA-Z0-9]{3,}\.[a-zA-Z]{2,}', email)

if match:
    print("Valid")
    print("Groups: ",match.group())
else:
    print("Not Valid")

