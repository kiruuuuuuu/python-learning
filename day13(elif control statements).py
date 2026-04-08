#                                              elif statements
# wap to check the given number is positive or negative or zero
num=-45
if num>0:
    print('number is positive')
elif num<0:
    print('number is negative')
else:
    print('zero')  # number is negative


# wap to check largest value among 2 values

a=99
b=45
if a>b:
    print(f'{a} is largest number')
elif b>a:
    print(f'{b} is largest number') # 99 is largest number

# wap to check the largest of 3 numbers 
a,b,c=95,96,97
if a>b and a>c:
    print(f'{a} is the largest number')

elif b>c and b>a:
    print(f'{b} is the largest number')

else:
    print(f'{c} is the largest number') # 97 is the largest number


# wap to check the smallest of 3 numbers without using else statement
a,b,c=95,96,97
if a<b and a<c:
    print(f'{a} is the smallest number')

elif b<c and b<a:
    print(f'{b} is the smallest number')

elif c<a and c<b:
    print(f'{c} is the smallest number')  # 95 is the smallest number


# wap to check the given character is uppercase or lower case or digit or special characters

char=input('enter the value to check the characters:')
if char>='A' and char<='Z':
    print(f'{char} is in upper case')
elif  char>='a' and char<='z':
    print(f'{char} is in lower case')
elif  char>='0' and char<='9':
    print(f'{char} is digit')
else:
    print(f'{char} is a special characters') # A is in upper case

# wap to perform ATM operations like deposit withdraw and check balance

balance=56000
print('ATM menu')
print('1.balance')
print('2.deposit')
print('3.withdraw')
choice=int(input('enter a choice from above options'))
if choice==1:
    print(f'{balance} is the bank balance')
elif choice==2:
    amount=int(input('enter the amount to be deposited'))
    balance=balance+amount
    print(f'Rs {amount} has been deposited ')
    print(f'after deposit updated balance rs Rs :{balance}')
elif choice==3:
    withdraw=int(input('enter amount to withdraw'))
    balance=balance-withdraw
    print(f'Rs {withdraw} has been sucussfully withdrawn ')
    print(f'after withdraw updated balance rs Rs :{balance}')
else:
    print('invalid choice')
