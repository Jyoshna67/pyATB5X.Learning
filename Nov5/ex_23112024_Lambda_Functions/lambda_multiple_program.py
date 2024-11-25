#Write a program to calculate Even and Odd.
def find_even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
find_even_odd(9)
#Lambda
check_even_odd=lambda num:"Even"if num%2==0 else "odd"
print(check_even_odd(4))

