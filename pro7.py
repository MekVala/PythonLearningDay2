# Demo Of Package and module

from demo.find_prime import  is_prime

x = input("Enter No: ")
if is_prime(x):
    print("Entered No Is Prime")
else:
    print("Entered No Is Not Prime")

