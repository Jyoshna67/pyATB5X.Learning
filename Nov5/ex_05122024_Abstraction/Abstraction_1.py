from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name=name
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Bark Bark")
obj_ref=Dog("beera")
obj_ref.make_sound()
