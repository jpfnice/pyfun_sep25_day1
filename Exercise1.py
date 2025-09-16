
"""
Write a Python script that prompts the user for a number and displays a message that does indicate if the number is odd or even.

Note: do consider 0 has being neither odd nor even.

After having tested a first number, the script should prompt the user for other numbers as long as he or she would like to.
"""

print("The purpose of the script is to test if numbers are odd or even")

while True:
    
    nb=input("Enter an int: ")
    nb=int(nb)
    
    if nb == 0:
        print(nb,"is neither or or even: it is zero")
    elif nb % 2  == 0 : # <=> elif nb % 2 == 1
        print(nb,"is even")
    else:
        print(nb,"is odd")
    
    ok=input("Do you want to test another number (Y/N) ? ")
    if ok == "N" or ok == "n": # if ok is equal to "N" or "n"
        break # Leave the while loop now !

print("Bye !")