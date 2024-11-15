s1=int(input("Enter the length of side1"))
s2=int(input("Enter the length of side2"))
s3=int(input("Enter the length of side3"))
if s1==s2==s3:
    print("The Triangle is,Equilateral")
elif s1==s2 or s2==s3 or s1==s3:
    print("The Triangle is,Isosceles")
else:
    print("The Triangle is,Scalene")

