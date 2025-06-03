
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

if "B" not in name:
    print("B is not in Hello")
    
data=["Hello", "abc", "the", "world"]
print("size of data:", len(data))

for element in data:
    print(element)

if "abc" in data:
    print("abc is in data")

d1=[23,45,67,23]
print(sum(d1), len(d1))
d2={23,45,67,23}
print(sum(d2), len(d2))




