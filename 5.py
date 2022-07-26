
# copy methode 

import copy
l1=[10,20,30,[40,50,60],70,80]
l2=copy.deepcopy(l1)
print('Before')
print(l1)
print(l2)
print('Do changes')

l1[3][0]='akshay'
print('After changing')
print(l1)
print(l2)