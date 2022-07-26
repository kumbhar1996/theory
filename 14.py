
# different method in the set

s={1,2,3,4}

# add fun used for to add the element at the end of set

s.add(5)
print(s)

# remove fun is used for to remove the specified element from set
s.remove(4)
print(s)

# clear is for to clear the all values

s.clear()
print(s)

# set comperhensive

x=range(1,6)

result={v**2 for v in x}
print(result)

# frozen set

s1={1,2,3,4}

s2=frozenset(s1)
print(s1)
print(s2)

s1.remove(2)
print(s1)
'''

s2.remove(2)
print(s2)   


 'frozenset' object has no attribute 'remove
 ''''