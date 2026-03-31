# datatypes in python


# single valued datatype
# int,float,complex,boolean

# integer datatype
a=98
print(a)
print(type(a))

b=int()
print(b)  # to display default value of int

# float datatype

c=98.48
print(c)
print(type(c))

d=float()
print(d)


# complex datatype

e='10+gj'
print(e)
print(type(e))

f=complex()
print(f)


# boolean datatype

g='true'
print(g)
print(type(g))

h=98
g='true'
print('g+h')  # true has 1 value and false ha 0 value so result is 99

i=bool()
print(i)
# multi valued datatypes
# string,list,tuple,set,dict



# string datatype

# indexing on string collecting datatype

# positive indexing
msg='python'
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[5])

# negative indexing

msg='python'
print(msg[-1])
print(msg[-2])
print(msg[-3])
print(msg[-4])
print(msg[-5])
print(msg[-6])

# combining 2 strings in indexing
s1='python'
print(s1[2]+s1[3])


# slicing 

# examples for positive slicing

string='welcome to python class'
print('positive slicing examples')
print(string[0:7])
print(string[8:10])
print(string[11:17])
print(string[18:23])
print(string[0:11])
print(string[11:23])
print(string[3:9])
print(string[5:15])
print(string[:7])
print(string[8:])

# examples for negative slicing

string='welcome to python class'
print('negative slicing examples')
print(string[-5:])
print(string[-12:-6])
print(string[-23:-16])
print(string[-15:-13])
print(string[-11:-7])
print(string[-23:-1])
print(string[:-6])
print(string[-6:])
print(string[-10:-5])

# example for reversing

string='welcome to python class'
print('examples for reversing')
print(string[::-1])
print(string[22::-1])
print(string[16:10:-1])
print(string[-1:-6:-1])
print(string[9::-1])

# wap to print even digit characters in forward direction

str='python class' 
print(str[0::2])

# wap to print even digit characters from string in backward direction

str='python class' 
print(str[-2::-2])

# wap to print odd digit characters from string in backward direction

str='python class' 
print(str[-1::-2]) # sacnhy

# wap to reverse a string

str='python class' 
print(str[::-1]) # ssalc nohtyp

# examples for positive slicing


print('positive slicing examples')
string='welcome to python class'
print(string[0:7])
print(string[8:10])
print(string[11:17])
print(string[18:23])
print(string[0:11])
print(string[11:23])
print(string[3:9])
print(string[5:15])
print(string[:7])
print(string[8:15])

# examples for negative slicing
print('negative slicing examples')
string='welcome to python class'
print(string[-5:])
print(string[-12:-6])
print(string[-23:-16])
print(string[-15:-13])
print(string[-11:-7])
print(string[-23:-1])
print(string[:-6])
print(string[-6:])  
print(string[-10:-5])

# example for reversing
print('examples for reversing')
string='welcome to python class'
print(string[::-1])
print(string[22::-1])
print(string[16:10:-1])
print(string[-1:-6:-1])
print(string[9::-1])

