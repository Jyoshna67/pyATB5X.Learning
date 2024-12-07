class SfLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg
    def login_confirm(self):
        if self.email=="jyoshreddy1@gmail.com" and self.password=="joo123":
            print("allowed","login successful")
        else:
            print("Login failed")

email=input("Enter your email")
password=input("Enter your password")
sfo_obj=SfLoginPage(email,password)
sfo_obj.login_confirm()


