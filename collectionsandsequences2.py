
"""
Collection: 
    list, tuple, set, dict, array, str, ...
    
    Sequences: collections with the concept of "position"
        list, tuple, str, array

"""

# first element of a sequence: [0]

text="Hello World"
print(text[0])

alist=[5,6,10,2,-3,2,10]
print(alist[0])

# last element of a sequence: [-1]

text="Hello World"
print(text[-1])
print(text[len(text)-1])

alist=[5,6,10,2,-3,2,10]
print(alist[-1])

# slice of a sequence: [start:stop] or [start:stop:inc]

text="Hello World"
print(text[2:7])
print(text[2:7:2])
print(text[:7])
print(text[3:])

alist=[5,6,10,2,-3,2,10]
print(alist[1:6])
print(alist[1:6:3])

# duplicating elements with *

text="AB"*10
print(text)
text="-"*80
print(text)

alist=[0]*100
print(alist)

# concatenating elements with +

text="ABC" + "DEF"
print(text)


alist=[3,4,5] + [10,11]
print(alist)





