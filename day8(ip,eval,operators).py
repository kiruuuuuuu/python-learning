# input statement in python

# number=input('enter a value :') # ip=2
# print(number) # 2
# print(type(number)) # <class 'str'>

# num=int(input('enter a value :'))
# print(num)
# print(type(num)) # <class 'int'>

# eval statement in python

# number1=eval(input('enter a value')) # eval changes to correct datatype
# print(number1)
# print(type(number1)) # <class 'int'>

# number1=eval(input('enter a decimal value')) # eval changes to correct datatype
# print(number1)
# print(type(number1)) # <class 'float'>

# operators in python
# 1.arithmetic operator(+,-,*,/,//,%,**)
# 2.relational operator(<,>,<=,>=,!=,==)
# 3.logical operators(and,or,not)
# 4.assignment operator(+=,-=,*=,/=,//=,%=,**=)
# 5.membership operator(in,not in)
# 6.identity operators(is,is not)

# arithmetic operators
# addition
a=98
b=67
result=a+b
print(result)

num1=99
num2=True
print(num1+num2) # 100

x=67
y=56.89
print(x+y) # 123.89

msg='smith is earning ' # concatination
sal=800
print(msg+str(sal)) # smith is earning800

l1=[10,20,30]
l2=[40,50,60]
print(l1+l2) # [10, 20, 30, 40, 50, 60]

num1=100
num2=10+0j
print(num1+num2) # (110+0j)

t1=(1,2,3)
t2=(10,20,30)
print(t1+t2) # (1,2,3,10,20,30)

# subtraction

no1=30
no2=20
print(no1-no2) # 10

# multiplication
print(3*2) #6
print(4*' python') #  python python python python

# true division
a=98
b=78
print(a/b) # 1.2564102564102564

# flo division
a=98
b=78
print(a//b) # 1

# wap to remove last digit from given number

num=8574848
print(num//10) # 857484

# wap to remove last two digit from given number

num=8574848
print(num//100) # 85748

# modules
a=11
b=2
print(a%b) # 1

# num1=56
# num2=0
# print(num1 % num2) # ZeroDivisionError: division by zero

# wap to display last digit from a given number

number=7689
print(number % 10) # 9

# wap to display last 3 digit from a given number

number=7689
print(number % 1000) # 689

# exponent

a=2
b=3
print(a**b) # 8
