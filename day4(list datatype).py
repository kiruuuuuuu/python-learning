# list datatype

# homogeneous collection in list

list1=[10,20,30,40,50]
print(list1)

# etherogeneous collection in list

list2=[90,'smith',True,100.98]
print(list2)

# indexing on list

list3=[90,'smith',98,100,'analyst']
print(list3[0])
print(list3[2])
print(list3[4])
print(list3[-3])
print(list3[-1])
# print(list3[9]) list index out of range


# example for indexing using nested list

nested=[10,20,30,'smith',[100,200,300],'analyst']
print(nested[4])     #  [100, 200, 300]
print(nested[4][1])  # 200
print(nested[4][-1]) # 300

# slicing on list datatype

# example for slicing using nested list

nested=[10,'smith',[100,200,300,400,500],'analyst']
print(nested[2][1:5:1])#[200, 300, 400, 500]
print(nested[2][0:2:1])#[100, 200]
print(nested[2][2:3:1])#[300]
print(nested[2][::-1])#[500, 400, 300, 200, 100]
print(nested[1:5:1][2]) #analyst

# postitive slicing examples

l1=[10,"python",3.14,True,[1,2,4],(5,6)]

