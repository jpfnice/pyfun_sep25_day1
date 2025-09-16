
"""
Collection: 
    list, tuple, set, dict, array, str, ...
    
    Sequences: collections with the concept of "position"
        list, tuple, str, array, ...

"""
import inspect
# first element of a sequence: [0]

text="Hello World"
print(inspect.currentframe().f_lineno, text[0])

alist=[5,6,10,"gg",-3,True,10] # a list is defined here
print(inspect.currentframe().f_lineno, alist[0])

# last element of a sequence: [-1]

text="Hello World"
print(inspect.currentframe().f_lineno, text[-1])
print(inspect.currentframe().f_lineno, text[10])
print(inspect.currentframe().f_lineno, "Length of text", len(text))
print(inspect.currentframe().f_lineno, text[len(text)-1])

alist=[5,6,10,2,-3,2,10]
print(alist[-1])

# slice of a sequence: [start:stop] or [start:stop:inc]

text="Hello World"
print(inspect.currentframe().f_lineno, text[2:7]) # 2,3,4,5,6 "llo W
print(text[2:7:2]) # 2,4,6
print(text[:7])# 0,1,..,6
print(text[3:]) # 3,4,5,...

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





