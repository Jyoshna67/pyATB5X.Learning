class Person:

    def __init__(self):
        self.name=input("Enter the name")
        self.age=input("Enter the age")
        self.phone=input("Enter the phone")
        self.occupation=input("Enter the occupation")

    def name_of_the_function_to_display(self):
        print(f"name is{self.name}",f"age is {self.age}",f"phone is {self.phone}",f"occupation is {self.occupation}")
person1=Person()
person1.name_of_the_function_to_display()












