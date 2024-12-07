from Nov5.ex_03122024_OOPS.Single_Inheritance import son_obj


class Father:
    def father_money(self):
        return 10

class Mother:
    def mother_money(self):
        return 5
class Son(Father,Mother):
    def info(self):
        print("Son")

s=Son()
print(s.father_money())
print(s.mother_money())
print(s.info())