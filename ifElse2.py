"""
if boolean condition:
    statement 1
    statement 2
    ...
else:
    statement 3
    statement 4
    ...
    
"""

num=input("Please enter an int: ")
num=int(num)

if num > 0: # > < >= <= == !=  ...
    print(num, "is positive")
else:
    print(num, "is negative or null")
    
print("The end")
