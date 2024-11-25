t1=(1,2,3,4)
#t1.append(2) #tuble object doesn't allow to add so we can change this tuple into "list".
my_list=list(t1)
my_list.append(5)
t1=tuple(my_list)
print(t1)