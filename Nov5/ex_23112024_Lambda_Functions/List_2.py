from os import remove

my_list=[1,2,3]

#append=add
my_list.append(4)
print(my_list) #output=[1,2,3,4]

#Extend
my_list.extend([5,6,7])
print(my_list) #output=[1,2,3,4,5,6,7]

#insert
my_list.insert(1,"Jyo")
print(my_list)

my_list[3]="reddy"
print(my_list)
#remove
my_list.remove("reddy")
print(my_list)

#copy list
my_copy_list=my_list.copy()
print(my_copy_list)
print(my_list)
print(my_copy_list)