# type casting in python

# implicit typecasting
# explicit typecasting


# example for implicit typecasting

a=98
b=35.67
print(a+b)  # 133.67000000000002

a=98
b=35.67
result=a+b
print(type(result))  # <class 'float'>

# explicit typecasting

# integer datatype typecasting
num=57
print(float(num)) # 57.0
print(complex(num)) # 57+0j
print(bool(num)) # true
print(str(num))  # '56'

# num=57
# print(list(num)) #type error
# print(tuple(num)) #type error
# print(set(num))   #type error
# print(dict(num))  #type error

# float datatype typecasting

num=89.56
print(int(num)) #89
print(complex(num)) #89.56+0j
print(bool(num)) # true
print(str(num))  # '89.56'

# num=89.56
# print(list(num)) #type error
# print(tuple(num)) #type error
# print(set(num)) #type error
# print(dict(num)) #type error

# complex datatype in typecasting

num=10+0j
print(bool(num)) # true
print(str(num)) # '10+0j'


# num=10+0j
# print(int(num)) # type error
# print(float(num)) # type error
# print(list(num)) # type error
# print(tuple(num)) # type error
# print(set(num)) # type error
# print(dict(num)) # type error
 
# boolean datatype in typecasting

a=True
print(int(a)) # 1
print(float(a)) # 1.0
print(complex(a)) # 10+0j
print(str(a)) # true

# a=True
# print(list(a)) # type error
# print(tuple(a)) # type error
# print(set(a)) # type error
# print(dict(a)) # type error

# string datatype in typecasting

