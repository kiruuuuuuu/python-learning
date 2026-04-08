# conditional statement
#                                  if statement

# wap to check greatest number among 2 numbers
a=78
b=45
if a>b:
    print(f'{a} is greater than {b}')


# wap to check the given number is positive

num=int(input('enter the number :'))
if num>0:
    print(f'{num} is a positive number')


# wap to check the given number is even digit

num1=44
if num1%2==0:
    print(f'{num1} is a even number')

# wap to check the given no is odd number

num1=45
if num1%2==1:
    print(f'{num1} is a odd number')

# wap to check the given no is divisible by 3 & 5

num2=15
if num2%3==0 and num2%5==0:
    print(f'{num2} is divisible by 3 & 5')


# wap to check the given string starts with vowels

s1='Air india'
if s1[0] in 'aeiouAEIOU':
    print(f'{s1} starts with vowels')

# using or

s1='Air india'
if s1[0]=='a' or s1[0]=='e' or s1[0]=='i'or s1[0]=='o'or s1[0]=='u' or s1[0]=='A' or s1[0]=='E' or s1[0]=='I' or s1[0]=='O' or s1[0]=='U':
    print(f'{s1} starts with vowels')

# wap to check the given string starts with consonents
s1='Microsoft'
if s1[0] not in 'aeiouAEIOU':
    print(f'{s1} starts with consonents')

# wap to check the given string starts with upper case

s1='Microsoft'
if s1[0] >='A' and s1[0]<='Z':
    print(f'{s1} starts with upper case')

# another method
s1='Microsoft'
if 'A'<=s1[0]<='Z':
    print(f'{s1} starts with upper case')

# wap to check the given data is single valued data

data=45
if type(data) in [int,float,complex,bool]:
    print(f'{data} is single value data')

# wap to check the given data is collection datatype

data=[10,20,30]
if type(data) in [str,list,tuple,set,dict]:
    print(f'{data} is collection datatype')

# wap to check the given string having more than 5 characters

s2='education'
if len(s2)>5:
    print(f'{s2} has more than 5 characters')

# wao to check the given no is divisible by 3 & 5 if it is converted in complex value 

num=15
if num%3==0 and num%5==0:
    print(complex(num))

# wap to check the given no is even if it is even then store digits in list

num=567
if num%2==0:
    print(list(str(num)))


# wap to check the given character is vowels if yes print the next character
ch='A'
if ch in 'aeiouAEIOU':
    next_char=chr(ord(ch)+1)
    print(next_char)

# wap to check the given character is vowels if yes print the before character
ch='a'
if ch in 'aeiouAEIOU':
    next_char=chr(ord(ch)-1)
    print(next_char)