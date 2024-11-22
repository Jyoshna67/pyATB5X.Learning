def add_Security(func):

    def wrapper():
        print("Before the function is called")
        print("2.Add helmet,gloves")
        func() #dribing_Scooty
        print("3.After the function is called")
        print("Safe driving")
    return wrapper()

@add_Security
def driving_scooty():
        print("This is normal function:")
        print("I am driving scooty")