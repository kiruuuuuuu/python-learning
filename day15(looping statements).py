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

