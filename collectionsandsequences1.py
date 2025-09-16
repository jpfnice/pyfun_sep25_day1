
"""
Collections: 
    list, tuple, set, dict, array, str, ...
    
    Sequences: collections with the concept of "position"
        list, tuple, str, array

function, statement and operators available to any collection: 
    len()
    sum(), min(), max() if the collection contains numeric values
    ...
    for loop
    in
    not in
    
"""

name="Hello"
print("size of name:", len(name))

for c in name:
    print(c)

data=[23,56,78,89,100]

# A for loop is used
total=0
for nb in data:
    total = total + nb
print(total)

# A while loop is used
total=0
index=0
while index < len(data):
    total=total+data[index]
    index = index + 1
print(total)

print(sum(data)) # min() max() sum()

name="Hello"
if "B" not in name:
    print("B is not in Hello")

name="Hello"
if "ll" in name:
    print("ll is in Hello")
    
data=["Hello", "abc", "the", "world"]
print("size of data:", len(data))

for element in data:
    print(element)

if "abc" in data:
    print("abc is in data")

d1=[23,45,67,23] # A list
print(d1)
print(sum(d1), len(d1))
print(d1[1])

s1={23,45,67,23} # A set
print(s1)
print(sum(s1), len(s1))









