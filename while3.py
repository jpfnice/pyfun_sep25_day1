"""
while boolean condition:
    statement 1
    statement 2
    if condition:
        break

"As long as boolean condition is True, the block of statement is executed"

"""


while True:
    
    nb=input("Enter an int: ")
    nb=int(nb)
    
    print("nb is",nb, "nb**3 is", nb**3)
    
    ok=input("Ok to continue (Y/N) ? ")
    if ok == "N": # if ok is equal to "N"
        break
    
print("The end")
    

