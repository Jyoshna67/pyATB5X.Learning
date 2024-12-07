class Father:
    key="2BHK"
    def house(self):
        print("2bhk")
        print(self.key)
class Son(Father):
       def house1(self):
        print("3BHK")
class Daughter(Father):
    key2="No House"
    def house2(self):
        print("No house")

d=Daughter()
print(d.house())
print(d.house2())
s=Son()
print(s.house())
print(s.house1())

