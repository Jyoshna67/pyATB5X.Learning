a=10     #Global variable
class Person:
    b=20   #Instance variable

    def print_scope(self):
        c=20           #Local variable
        print(c)
        print(self.b)
        a1="hello"
        print(a1)
        global a

object_ref=Person()
object_ref.print_scope()

