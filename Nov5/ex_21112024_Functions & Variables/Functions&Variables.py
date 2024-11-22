pb_global_b=12

def myfunction():
    pb_a=10
    print(pb_a)
    print(pb_global_b)
myfunction()
#print(pb_a)---->we can't print this we declared it as "inside"
print(pb_global_b)

#Output=10 10 12