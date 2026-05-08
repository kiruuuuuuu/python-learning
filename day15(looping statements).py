# 1.while loop, 2. for loop

# wap to print natural numbers from 1 to 5 
i=1
while i<=5:
    print(i)
    i=i+1
else:
    print('loop is completed') # loop is completed

# wap to print numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i=i-1  
else:
    print('loop is completed') # loop is completed


# wap to print even numbers from 1 to 10
i=1
while i<=10:
    if i%2==0:
        print(i,end=' ') # 2 4 6 8 10
    i=i+1


# wap to print odd numbers from 1 to 10
i=1
while i<=10:
    if i%2==1:
        print(i,end=' ') # 1 3 5 7 9
    i=i+1

# wap to print hello python 3 times
i=1
while i<=3:
    print('\nhello python')
    i=i+1

# wap to print given table
num=5
i=1
while i<=10:
    print(f'{num} x {i} = {num*i}')
    i=i+1

# wap to print sum of starting 5 natural numbers
i=1
total=0
while i<=5:
    total=total+i
    i=i+1
print(f'total sum of 5 natural numbers are {total}')

# wap to find sum of even digit number from 1 to 20
i=2
total=0
while i<=20:
    total=total+i
    i=i+2
print(f'sum of even numbers from 1 to 20 is {total}')

# wap to find no of digits present in a given number
number=43879
count=0
while number>0:
    number=number//10
    count=count+1
print(f'number of digits present in the given number is {count}')

#  wap to print elements of list are even or odd numbers
list=[23,44,65,78,90]
i=0
while i<len(list):
    if list[i]%2==0:
        print(f'{list[i]} is even number')
    else:
        print(f'{list[i]} is odd number')
    i=i+1

# wap to print numbers which are divisible by 3 from 1 to 10
num=1
while num<=10:
    if num%3==0:
        print(f'{num} is divisible by 3')
    else:
        print(f'{num} is not divisible by 3')
    num=num+1

# wap to print numbers are divisible by 3 and 5
num=1
while num<=20:
    if num%3==0 and num%5==0:
        print(f'{num} is divisible by 3 and 5')
    num=num+1

# wap to print numbers whose last digit is present between 6 to 9 from 25 to 30
num=25
while num<=30:
    if num%10 in (6,7,8,9):
        print(f'{num} ends in 6,7,8,9')
    else:
        print(f'{num} does not ends in 6,7,8,9')
    num=num+1

# wap to print even digit numbers from given number
number=5643876
while number>0:
    digit=number%10
    if digit%2==0:
        print(f'{digit} is a even number')
    number=number//10

# wap to print even digit number from the given number and if the digit is greater than 4 

number=5643876
while number>0:
    digit=number%10
    if digit%2==0 and digit>4:
        print(f'{digit} is a even number')
    number=number//10

# wap to print digit which are greater than 4 from given number

num=59732382
while num>0:
    digit=num%10
    if digit>4:
        print(f'{digit} is greater than 4')
    num=num//10


# wap to find sum of all the digits from given number

number1=56832829
total=0
while number1>0:
    digit=number1%10
    total=total+digit
    number1=number1//10
print(f'sum of all the given number is {total}')

# wap to print sum of even digits from given number

number1=56832829
total=0
while number1>0:
    digit=number1%10
    if digit%2==0:
        total=total+digit
    number1=number1//10
print(f'sum of all the given even digit numbers is {total}')

# wap to find product of digits from given number

num=5748483
product=1
while num>0:
    digit=num%10
    product=product*digit
    num=num//10
print(f'product of given number is {product}')

# wap to print sum of all digits and product of all digits

num=573847847
total=0
product=1
while num>0:
    digit=num%10
    total=total+digit
    product=product*digit
    num=num//10
print(f'sum of all the given number is {total}')
print(f'product of given number is {product}')


# wap to find sum of even digits and product of odd digits from a given number

num=573847847
total=0
product=1
while num>0:
    digit=num%10
    if digit%2==0:
        total=total+digit
    else:
        product=product*digit
    num=num//10
print(f'sum of all the given number is {total}')
print(f'product of given number is {product}')

# wap to print sum and product of even digits and odd digits without using else statement

num=573847847
totaleven=0
producteven=1
totalodd=0
productodd=1
while num>0:
    digit=num%10
    if digit%2==0:
        totaleven=totaleven+digit
        producteven=producteven*digit

    elif digit%2==1:
        totalodd=totalodd+digit
        productodd=productodd*digit
    num=num//10
print(f'sum of all the given even number is {totaleven}')
print(f'product of given even number is {producteven}')
print(f'sum of all the given odd number is {totalodd}')
print(f'product of given odd number is {productodd}')