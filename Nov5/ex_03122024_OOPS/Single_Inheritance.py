class Father:
    key="2BHK"
    def car(self):
        print("My father has 2bhk house")
        print(self.key)

class Son(Father):  #Single Inheritance
    key1="3BHK"
    def suv(self):
        print("My son has 3bhk house")
        print(self.key1)
father_obj=Father()
father_obj.car()
son_obj=Son()
son_obj.suv()
print(son_obj.key)   #to access father properties
