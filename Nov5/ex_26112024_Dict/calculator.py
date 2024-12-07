class Cal:

           def __init__(self):
            print("DC")

            def sum(self,a,b):
                 return a+b
            def mul(self,a,b):
              return a*b
            def sub(self,a,b):
              return a-b
            def div(self,a,b):
               return a/b
object_ref=Cal()
a=float(input("Enter the number"))
b=float(input("Enter the number"))
output_sum=object_ref.sum(a,b)
output_sum=object_ref.sub(a,b)
output_sum=object_ref.mul(a,b)
output_sum=object_ref.div(a,b)-