#Static method->no need to create object reference we can call by using class name and method name.
class O:
    @staticmethod
    def sum(a,b):
        return a+b
print(O.sum(a=1,b=3))


