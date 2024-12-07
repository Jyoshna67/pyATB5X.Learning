class BaseTest:
    def open_browser(self):
        print("Browser is started")
    def close_browser(self):
        print("Broswer is closed")
class Testcase1(BaseTest):
    def positive(self):
        self.openbrowser()
        print("T1is executed")
        self.close_browser()
class Testcase2(BaseTest):
    def positive1(self):
        self.openbrowser()
        print("T2is executed")
        self.close_browser()

t=Testcase1
print(t.positive)


