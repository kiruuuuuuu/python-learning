# count method
t1=(10,20,20,30,20,40,20)
print(t1.count(20)) # 4

t2=('smith',98,'smith')
print(t2.count('smith')) # 2

# index method
t1=(10,20,20,30,20,40,20)
print(t1.index(20)) # 1

t1=(10,20,20,30,20,40,20)
first=t1.index(20)
second=t1.index(20,first+1)
print(second) # 2

# wap to find position of third occurence element from tuple collection using enumerate function

t1=(10,20,20,30,20,40,20)
element=20
c_value=0
for index,value in enumerate(t1):
    if value==element:
        c_value=c_value+1
        if c_value==4:
            print(index) # 6
            break




# sets inbuilt methods

# add method 
s1={'google','apple'}
s1.add('microsoft')
print(s1) # {'google', 'microsoft', 'apple'}

# remove method

s1={'google','apple','microsoft'}
s1.remove('microsoft')
print(s1) # {'apple', 'google'}

# update method

myset={'google','apple'}
anotherset={'microsoft'}
s1.update(anotherset)
print(s1) # {'apple', 'google','microsoft'}

# pop method
s1={'google','apple','microsoft'}
s1.pop()
print(s1) # {'apple', 'microsoft'}

# clear method

s1={'google','apple','microsoft'}
s1.clear()
print(s1) # set()


# union method

myset={1,2,3,4}
anotherset={3,4,5,6}
myset.union(anotherset) # {1, 2, 3, 4, 5, 6}


# intersection method

myset={1,2,3,4}
anotherset={3,4,5,6}
myset.intersection(anotherset) # {3, 4}

# difference method

myset={1,2,3,4}
anotherset={3,4,5,6}
myset.difference(anotherset) # {1, 2}

# symmetric difference method

myset={1,2,3,4}
anotherset={3,4,5,6}
myset.symmetric_difference(anotherset) # {1, 2, 5, 6}