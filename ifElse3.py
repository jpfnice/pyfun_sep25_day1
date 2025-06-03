"""
if boolean condition 1:
    statement 1
    statement 2
    ...
elif boolean condition 2:
    statement 3
    statement 4
    ...
elif boolean condition 3:
    statement 5
    statement 6
    ...
else:
    statement 7
    statement 8
    ...   
"""

num=input("Please enter an int: ")
num=int(num)

if num > 0: # > < >= <= == !=  ...
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
elif num == 0:
    print(num, "is zero")
    
print("The end")
