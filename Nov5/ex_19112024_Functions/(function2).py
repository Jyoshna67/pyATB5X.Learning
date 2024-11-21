#function within function
def greet_to_hello():
    print("Hello,welcome")


def greet():
        print("Hola")
        greet_to_hello()
greet_to_hello()
greet()
