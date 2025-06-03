
"""
Write a Python script that prompts the user for a number and displays a message that does indicate if the number is odd or even.

Note: do consider 0 has being neither odd nor even.

After having tested a first number, the script should prompt the user for other numbers as long as he or she would like to.
"""

num=input("Please enter an int: ") # input() returns a str
num=int(num) # int() converts a value into an int

# if num==0:
#     print("The number entered is 0")
# elif num%2==0:
#     print("The number entered",num," is even")
# elif num%2==1:
#     print("The number entered",num," is odd")

if num==0:
    print("The number entered is 0")
elif num%2==0:
    print("The number entered",num," is even")
else:
    print("The number entered",num," is odd")