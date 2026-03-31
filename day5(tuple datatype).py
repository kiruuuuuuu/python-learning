# tuple datatype


#                     example for homogeneous collection in tuple
t1=(10,20,30,98)
print(t1)

#                       example for etherogeneous collection
t2=(10,'smith',98.95, True, (10,20,30),[900,100])
print(t2)

# indexing on tuple datatype

tuple=(100,900,500,400,350,980,298)
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
print(tuple[4])
print(tuple[5])
print(tuple[-7])
print(tuple[-4])
#print(tuple[9]) #index out of range error

# examples for positive slicing in tuple

t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[0:5:1])
print(t1[1:7:1])
print(t1[2:8:2])
print(t1[0:9:3])
print(t1[3:9:2])
print(t1[4:9:1])
print(t1[1:9:2])
print(t1[0:8:4])
print(t1[2:9:3])
print(t1[5:9:1])

# examples for negative slicing in tuple

print('examples for negative slicing in tuple')
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[-9:-1:1])
print(t1[-8:-2:1])
print(t1[-7:-1:3])
print(t1[-6:-2:1])
print(t1[-5:-1:2])
print(t1[-9:-3:2])
print(t1[-8:-1:1])
print(t1[-7:-3:2])
print(t1[-6:-1:2])
print(t1[-4:-1:1])

# examples for reverse slicing in tuples

print('examples for reverse slicing in tuples')
t1=(900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[8:0:-1])
print(t1[8:2:-2])
print(t1[7:1:-1])
print(t1[8:-1:-1])
print(t1[6:0:-2])
