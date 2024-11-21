#write a program to sum of three inputs from the user input.
#If user doesn't enter any number,use default as (100,200,300)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
def sum_three(n1=100,n2=200,n3=300):
        return n1+n2+n3
result=sum_three(num1,num2,num3)
print(result)
#output: Enter first number=10
#Enter second number=20
#Enter third number=20
#50
result2=sum_three()
print(result2)
#output=600


