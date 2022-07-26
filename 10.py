
# Touple is immutable in nature
# we can not change the elements in the tuple


# creation of tuple 

elements=('akshay',10,12.2,'True','None')

print(elements)
print(type(elements))

nos=range(1,10)
result=tuple(nos)
print(result)

name=('sachin')
print(type(name))  # str

# Access the data from tuple 
'''
1. by using index 
2. by using slicing 
'''
print(elements[0])
print(elements[-1])

# we can convert the range into tuple

x=range(0,10)
print(type(x))

result=tuple(x)
print(result)
print(type(result))

# by using slicing

l=(10,20,30,40,50,60)
print(l[0:5:2])
print(l[:4:])
print(l[::2])
print(l[::])
print(l[:])

# reverse the tuple 
print(l[::-1])

# Touple comperhensive

x=range(1,10)
result=(x**2 for x in x)
print(tuple(result))

# mathematical operation 

t1=(1,2,3)
t2=(4,5,6)

t3=t1+t2
print(t3)   # touple addition

print(t3*4)  
