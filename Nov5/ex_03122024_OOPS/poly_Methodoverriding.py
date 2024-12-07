class Father:
    def home(self):
        print("2BHK")
class Son(Father):
    def home(self):
        print("3BHK")
s=Son()
print(s.home())
#ouput=3BHK(preference to local variable first)