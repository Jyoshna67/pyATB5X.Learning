def add_before_ui_after_ui(func):

    def wrapper():
        print("I'll set up the browser")
        print("I'll check the testcases")
        func() #test_ui
        print("Testcases are successfully executed")
        print("Quit the browser")
    return wrapper()
@add_before_ui_after_ui
def test_ui():
       print("I'll start the execution")