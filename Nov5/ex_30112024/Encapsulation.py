class Car:

       def __init__(self,o_name,o_model,o_make):
                     self.name=o_name
                     self.model=o_model
                     self.make=o_make

       def start_engine(self):
           print("Starting a car with the name"+self.name)
           print("Starting a car with the name" + self.model)
           print("Starting a car with the name" + self.make)

lambo=Car(o_name="lambo",o_model="v6",o_make="2024")
lambo.start_engine()



