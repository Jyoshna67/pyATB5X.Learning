#1 They don't return anything
#no return type, no parameter/argument


def greet():
    print("Hello World!")
greet()
#output=Hello world

#2 No return type, with parameter/argument
def greet_by_name(name):
    print("Hello",name)
greet_by_name("jooshu")
#output=Hello jooshu

#3 No return type,with default argument(#Positional argument)
def say_hello_default_arg(name="dileep"):
    print("Hello",name.upper())
say_hello_default_arg("jyo")
say_hello_default_arg()
#Output=Hello JYO
#Output=Hello DILEEP

#ex:2
def multiple_Args(name1="A", name2="B"):
    print("MUL->",name1,name2)
multiple_Args()
#output= MUL->A,B
multiple_Args("jyo")
#output=MUL1->jyo B

#4 Return type and argument
def sum_of_two(a,b):
    return a+b
result=sum_of_two(3,4)
print(result)
