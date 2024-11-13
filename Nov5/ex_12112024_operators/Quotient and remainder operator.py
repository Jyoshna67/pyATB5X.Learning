# //--> Quotient
# %-->Remainder
#method 1
num1=int(input("Enter your num1"))
num2=int(input("Enter your num2"))
Quotient=num1 // num2
Remainder=num1 % num2
print ("Quotient is",Quotient)
print ("Remainder is",Remainder)
#method 2
result=divmod(num1,num2)
print("result is",result)


