

# List Data types 

# list creation

players=['akshay','raveena','sachin']
print(players)
print(type(players))

# create list by using range

nos=range(1,10)
print(type(nos))

print(list(nos))
print(type(nos))

# or we can also create list by using range
result=list(nos)
print(result)
print(type(result))

# access the data from from list 
'''
1. by using index
'''

l1=['akshay',10,15.5,'True','None']
print(l1[0])
print(l1[-1])

'''
2.by using slicing
'''
print(l1[0:3])
print(l1[0:4:2])
print(l1[0:])
print(l1[::])

# print resverse the list 

print(l1[::-1])
l1.reverse()
print(l1)

# find the lenth of list 

print(len(l1))

# find the how many times chracter is coming in the list

print(l1.count('akshay'))

# list is mutable in nature 

l1[0]='Shilpa'
print(l1)

# Shallow copy 

l2=l1
print(l2)

# we can also copy by using copy function 
import copy
l3=copy.copy(l1)
print(l3)

# we can change the element

l3[0]='Dravid'
print(l3)



