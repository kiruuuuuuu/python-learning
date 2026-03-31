#                            set datatype in python

s1={10,20,30,40,20,20,98}
print(s1) # {50, 20, 40, 10, 60, 30}

s1={10,20,30,40,20,20,98}  # set removes duplicate values
print(type(s1)) # <class 'set'>

# example for indexing on set

s2={100,980,400,390,578}
# print(s2[3])  # TypeError: 'set' object is not subscriptable

s2={100,980,400,390,578}
li=list(s2)
print(li)  # [400, 578, 100, 980, 390]
print(type(li)) # <class 'list'>


#                           dict dataype in python

data={'ename':'smith','sal':98000,'job':'analyst'}
print(type(data))  #  <class 'dict'>
print(data['ename']) # smith
print(data['sal'])  # 98000
print(data['job'])  # analyst

print(f'employee name {data['ename']} and works as {data['job']} and salary is {data['sal']}')
# employee name smith and works as analyst and salary is 98000

#                        wap to store multiple employees information

employee={
    'emp1':{'ename':'smith','sal':980,},
    'emp2':{'ename':'allen','sal':5000},
    'emp3':{'ename':'king','sal':1250}
}
print(employee['emp3'])  # {'ename': 'king', 'sal': 1250}
print(employee['emp3']['ename'])  # king



#                           range datatype in python

coll=range(6)
print(coll) #range(0, 6)
print(list(coll)) # [0, 1, 2, 3, 4, 5]

e1=range(10,16)
print(list(e1)) # [10, 11, 12, 13, 14, 15]

e2=range(1,11,1)
print(list(e2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

e3=range(10,5,-1)
print(list(e3)) # [10, 9, 8, 7, 6]

e4=range(10,56,6)
print(list(e4))  # [10, 16, 22, 28, 34, 40, 46, 52]


# example for indexing using range datatype

nums=range(100,501,100)
print(type(nums)) # <class 'range'>
print(list(nums)) # [100, 200, 300, 400, 500]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[4])
print(nums[2])
# print(nums[9]) # IndexError: range object index out of range