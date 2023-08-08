
from test_calculator import TestFunctions
from test_get_digit import TestGetDigit
from test_operator import TestOperator
import HTMLTestRunner
import unittest

def Suite():
    SuiteTest = unittest.TestSuite()
    SuiteTest.addTest(TestFunctions("test_calculate_sin"))
    SuiteTest.addTest(TestFunctions("test_calculate_cos"))
    SuiteTest.addTest(TestFunctions("test_clear"))
    SuiteTest.addTest(TestFunctions("test_backspace"))
    SuiteTest.addTest(TestGetDigit("test_get_digit"))
    SuiteTest.addTest(TestOperator("test_calculate_addition"))
    SuiteTest.addTest(TestOperator("test_subtraction"))
    SuiteTest.addTest(TestOperator("test_multiplication"))
    SuiteTest.addTest(TestOperator("test_divison"))
    SuiteTest.addTest(TestOperator("test_square_root"))
    SuiteTest.addTest(TestOperator("test_cube_root"))
    return SuiteTest

if __name__=="__main__":
   filepath=r"C:\Users\u5550\Desktop\calculator_GUI\Calculator_HTML_Report.html"
   fp=open(filepath,'wb')
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Calculator_Report',description=u'Test report For calculator by SASHIT SHARMA')
   runner.run(Suite())
   fp.close()