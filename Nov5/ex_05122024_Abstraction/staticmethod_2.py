class Excelreader:
    @staticmethod
    def read_from_excel():
        print("reading from excel")
class TC1:
    def test_case(self):
        Excelreader.read_from_excel()
tc_obj=TC1()
tc_obj.test_case()