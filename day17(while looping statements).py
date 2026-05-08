# wap to check the given number is prime number or not
num=3
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
 
# or another method to find prime numbers
num=6
i=2
count=0
while i<num:
    if num%i==0:
        count=count+1
    i=i+1
if count==0 and num>1:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

# wap to print prime numbers between 1 to 30
num=1
while num<=30:
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print(num,end=' ')
    num=num+1

# wap to check the given number is amstrong number or not

num=153
temp=num
sumcubes=0
length=len(str(num))
while num>0:
    digit=num%10
    sumcubes=sumcubes+digit**length
    num=num//10
if temp==sumcubes:
    print(f'\n{temp} is a amstrong number')
else:
    print(f'\n{temp} is not a amstrong number')

# wap to print armstrong numbers from 100 to 10000 range

num=100
while num<=10000:
    temp=num
    sumcubes=0
    length=len(str(num))
    while temp>0:
        digit=temp%10
        sumcubes=sumcubes+digit**length
        temp=temp//10
    if num==sumcubes:
        print(f'{num} is armstrong number')
    num=num+1

# wap to print fibonacci series up to n terms
num=10
a,b=0,1
count=0
while count<num:
    print(a,end=' ')
    a,b=b,a+b
    count=count+1

# wap to check the given number is neon number or not
num=9
square=num*num
sumdigits=0
temp=square
while temp>0:
    digit=temp%10
    sumdigits=sumdigits+digit
    temp=temp//10
if num==sumdigits:
    print(f'\n{num} is a neon number')
else:
    print(f'\n{num} is not a neon number')

# wap to print neon numbers from 1 to 1000
num=1
while num<=1000:
    square=num*num
    sumdigits=0
    temp=square
    while temp>0:
        digit=temp%10
        sumdigits=sumdigits+digit
        temp=temp//10
    if num==sumdigits:
        print(f'{num} is a neon number')
    num=num+1

# wap to print sum of all the elements  present in the list
list=[23,44,65,78,90]
i=0
result=0
while i<len(list):
    result=result+list[i]
    i=i+1
print(f'Sum of all elements in the list: {result}')

# wap to find factorial of a given number
num=5
factorial=1
while num>0:
    factorial=factorial*num
    num=num-1   
print(f'factorial of the given number is {factorial}')

# wap to print ascii  values of characters from a given string
string='python'
i=0
while i<len(string):
    print(f'ascii value of {string[i]} is {ord(string[i])}')
    i=i+1

# wap to convert string to uppercase without using inbuilt function
string='python'
i=0
result=''
while i<len(string):
    if 'a'<=string[i]<='z':
        result=result+chr(ord(string[i])-32)
    else:
        result=result+string[i]
    i=i+1
print(f'Uppercase of {string} is {result}')

# wap to convert string to lowercase without using inbuilt function
string='PYTHON'
i=0
result=''
while i<len(string):
    if 'A'<=string[i]<='Z':
        result=result+chr(ord(string[i])+32)
    else:
        result=result+string[i]
    i=i+1
print(f'Lowercase of {string} is {result}')

# wap to convert lowercase to uppercase and uppercase to lowercase without using inbuilt function(toggle case)
string='PyThOn'
i=0
result=''
while i<len(string):
    if 'a'<=string[i]<='z':
        result=result+chr(ord(string[i])-32)
    elif 'A'<=string[i]<='Z':
        result=result+chr(ord(string[i])+32)
    else:
        result=result+string[i]
    i=i+1
print(f'Toggle case of {string} is {result}')

# wap to find the number of characters present in the given string without using inbuilt function
string='python programming'
i=0
count=0
while i<len(string):
        count=count+1
        i=i+1
print(f'Number of characters in {string} is {count}')

# wap to find occurance of a given character in the given string without using inbuilt function
s='pyspiders'
char='s'
i=0
count=0
while i<len(s):
    if s[i]==char:
        count=count+1
    i=i+1
print(f'Occurrence of {char} in {s} is {count}')