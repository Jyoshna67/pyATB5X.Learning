#to handle exception we have to use "try and except".
try:
    num1=int(input("enter the number1"))
    num2=int(input("enter the number2"))
    result=num1/num2
except Exception as e:
    print(e)
#another example
try:
    num1=int(input("Enter the value"))
    num2=int(input("Enter the value"))
    result=num1/num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("output is", result)
finally:   #It will execute always whether program pass/fail
    print("This code always executed")
