
"""
set:
    a set is a collection but nor a sequence
    a set is a collection that does not accept duplicated elements
"""

s1={2,3,4,3,3,10,2}
print(s1, len(s1), type(s1))

s1=set([3,5,3,5,8])
print(s1, len(s1), type(s1))

s1=set()
print(s1, len(s1), type(s1))

s1={2,3,4,3,3,10,2}

s1.add(56)

for e in s1:
    print(e)
    
s2={4,10,12,13}   
print(s1, s2)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))