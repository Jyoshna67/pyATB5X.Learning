#Multilevel GF->F->C
class Grandfather:
    Gold="2kg"
    def gram(self):
        print("Grandafther has gold")
        print(self.gram)

class Father(Grandfather):
    Silver="3kg"
    def gram1(self):
        print("My father has silver")
        print(self.gram1)
class Son(Father):
    Diamond="10kg"
    def gram2(self):
        print("My son has Diamond")
        print(self.gram2)

father_obj=Father()
father_obj.gram()
father_obj.gram1()
son_obj=Son()
son_obj.gram2()

