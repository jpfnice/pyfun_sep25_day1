"""
list
"""
# Creation:
    
data=[5,6.7,True,"abc"]
print(data, type(data))

data=[5, 5.6, True, 23.3j, [0,1]]
print(data, len(data), type(data))

data=list() # <=> data=[]
print(data, len(data), type(data))

data=list("abcdef") 
print(data, len(data), type(data))

# How to update a list:

data=[5,6,7,8]
print(data, type(data))
data[-1]=25 # <=> data[3]=25
print(data, type(data))

data.append(100) # append() is a "method"
print(data, type(data))

data.insert(0, True)
print(data, type(data))

data.append([20,30,40])
print(data, type(data))

data.extend([20,30,40])
print(data, type(data))

data.pop(0)
print(data, type(data))

data.pop()
print(data, type(data))

data.remove(25)
print(data, type(data))

del data[0:3]
print(data, type(data))

data.clear()
print(data, type(data))

# Other methods

data=[4,-2,6,-4,10, -2,-4]
print(data)

data.sort()
print(data)

data.reverse()
print(data)

print("Position of -2 is", data.index(-2))
print("How many time does -2 appear ?", data.count(-2))

# and also: for, in, not in, len(), ...
