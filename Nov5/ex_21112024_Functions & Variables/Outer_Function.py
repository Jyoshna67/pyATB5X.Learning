def outer_function():
    var1=30  #local variable
    def inner_function():
        print(var1)
    def inner_function1():
        print(var1)

    inner_function()
    inner_function1()
outer_function()

#output=30 30
