# append method
list=[45,98,100]
list.append(50)
print(list) # [45, 98, 100, 50]

# ex 2
list=[45,98,100]
list.append([50,60,70,80]) # [45, 98, 100, [50, 60, 70, 80]]
print(list)

# extend method

li=[20,40,60,80,100]
li.extend([120,140,160])
print(li) # [20, 40, 60, 80, 100, 120, 140, 160]


# insert method
li=[20,40,80,100]
li.insert(2,60)
print(li) # [20, 40, 60, 80, 100]

# count method

li=[10,20,40,20,50,20,30]
print(li.count(20)) # 3

# index method

li=[10,20,40,20,50,20,30]
print(li.index(20)) # 1

# li=[10,20,40,20,50,20,30]
# print(li.index(98)) # ValueError: list.index(x): x not in list

# reverse method
li=[1,2,3,4,5]
li.reverse()
print(li) # [5, 4, 3, 2, 1]

# sort method

# example for ascending
li=[10,43,2,4,6,7,3,1,233,44,666]
li.sort()
print(li) # [1, 2, 3, 4, 6, 7, 10, 43, 44, 233, 666]

# example for descending
li=[10,43,2,4,6,7,3,1,233,44,666]
li.sort(reverse=True)
print(li) # [666, 233, 44, 43, 10, 7, 6, 4, 3, 2, 1]



# pop method
li=[1,2,3,4,5,6,7]
li.pop()
print(li) # [1, 2, 3, 4, 5, 6]


li=[1,2,3,4,5,6,7]
li.pop(5)
print(li) # [1, 2, 3, 4, 5, 7]

# remove method

li=[1,2,3,4,5,6,7]
li.remove(5)
print(li) # [1, 2, 3, 4, 6, 7]

# clear method

li=[1,2,3,4,5,6,7]
li.clear()
print(li) # []


# wap to find position of 4th occurance of element using enumerate function

data=[10,20,30,20,40,20,50,20,98]
element=20
count=0
for index,value in enumerate(data):
    if value==element:
        count=count+1
        if count==4:
            print(index)
            break


# wap to find third highest element using enumerate

data=[10,20,30,20,40,20,50,20,98]
numbers=list(set(data))
numbers.sort(reverse=True)
for index,value in enumerate(numbers,start=1):
    if index==3:
        print(f'third highest element : {value}')
        break

# # wap to check the given no is palindrome,armstrong,strong no 
# # using only one while loop and one block

num=int(input('enter a number'))
original=num
temp=original
reverse=0
armstrong_sum=0
strong_sum=0
length=len(str(num))

while temp>0:
    digit=temp%10
    # palindrome logic
    reverse=reverse*10+digit

    # armstrong logic
    armstrong_sum=armstrong_sum+digit**length
    # strong logic
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
        strong_sum=strong_sum+fact
    temp=temp//10

if reverse==original:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not a palindrome')

if armstrong_sum==original:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not a armstrong number')

if strong_sum==original:
    print(f'{num} is strong number')
else:
    print(f'{num} is not a strong number')
