#                                    if else statements
# wap to check the given no is even or odd

num=97
if num%2==0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')

# wap to check the given no is positive or negative

num=97
if num>0:
    print(f'{num} is a positive number')
else:
    print(f'{num} is a negative number')


# wap to check the given character is upper case or not

ch='A'
if ch>='A' and ch<='Z':
    print(f'{ch} is upper case')
else:
    print(f'{ch} is not upper case')

# wap to check the given character is lower case or not

ch='g'
if ch>='a' and ch<='z':
    print(f'{ch} is lower case')
else:
    print(f'{ch} is not lower case')

# wap to check the given year is leapyear or not

year=2024
if(year%400==0) and (year%4==0 or year%100!=0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


# wap to check the given collection data is a collection datatyoe or not

data=[10,20,30,40]
if type(data) in [str,list,tuple,set,dict]:
    print(f'{data} is a collection datatype')
else:
    print(f'{data} is not a collection datatype')

# wap to remove the duplicate elements from given data if the data is collection datatype

data=[10,20,30,40,10,20]
if type(data) in [str,list,tuple,set,dict]:
    print(list(set(data)))
else:
    print(data)

# wap to check the given value is string datatype or not

value='smith'
if type(value)==str:
    print(f'{value} is a string')
else:
    print(f'{value} is not a string')

# wap to check the given data is palindrome or not

s1='python'
if s1==s1[::-1]:
    print(f'{s1} is a palindrome')
else:
    print(f'{s1} is not a palindrome')

# wap to perform check balance and deposit operation

balance=58000
deposit=3000

if deposit>0:
    balance=balance+deposit
    print(f'{deposit} is deposited to the bank account and updated balance is rs :{balance}')
else:
    print('deposit amount should be greater than zero')


# wap to perfrom withdraw operation

balance=67000
withdraw=int(input('enter the amount to be withdrawed :'))
if balance>withdraw:
    balance=balance-withdraw
    print(f'rs {withdraw} has succussfully been withdrawed and updated balance is rs : {balance}')
else:
    print('insufficient balance')
