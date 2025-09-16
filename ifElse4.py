

"""
I want to test that an int is in the range [10,45[
    
"""

num=input("Please enter an int: ")
num=int(num)

print(num >= 10 and num < 45) # print True or False

if num >= 10 and num < 45: # If the condition is True

    print(num,"is in the range: [10,45[")
    
else:# If the condition is False

    print(num,"is not in the range: [10,45[")