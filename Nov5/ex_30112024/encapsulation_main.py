class Login:

    def __init__(self):
        self.password="joo" #public instance variable
        self.__password_Secure="jyosh"  #Private Instance Variable(Encapsulation if we use  double underscore it's private

    def change_password(self):
        print(self.password)
obj_ref=Login()
print(obj_ref.change_password)