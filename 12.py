

# String 
'''
1. string can written in side the single or double coat in python
'''
name='aksahy'
lastname="kumbhar"
print(name)
print(lastname)

name='''ak'''
print(name)

# formating the string by using dynamic value

name='akshay'
lastname='kumbhar'
age=25

print('my name is {} ,my last name is {} and my age is {} '.format(name,lastname,age))
print('my name is {0}, my last name is {1} and my age is {2} '.format(name,lastname,age))
print('my name is {z}, my lastname is {y} and my age is {x}'.format(x=age,y=lastname,z=name))

# split the string 
'''
split function do the elements separaetly by using comma
'''

s='python is a programing language'
print(s)
print(type(s))

print(s.split())

# replace method 
# i want to replace the python with java

result=s.replace('python','java')
print(result)

# count method
'''
count method count the given element how many times it come inside the string
'''

print(s.count('python'))
print(s.count('Python'))

# find method it shows the index of initial letter in the string 

x='hi this is akshay,i am from pune'

print(x.find('akshay'))
print(x.find('hi'))

print(x.find('Hi'))   # Case sensitive -1 shows when given element is not present in the string
'''
1. in find function if given element is present then it give the initial index value of element 
2. if given element is not present then it give -1
'''
# index()

print(x.index('akshay'))

print(x.index('Akshay'))

'''
1. in index function if given element is present in the string then it shows the initial index of given letter
2. if element not present then got message substring not found
'''