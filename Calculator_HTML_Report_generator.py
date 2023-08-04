
from test_calculator import TestCalc
from test_get_digit import TestCalculator
from test_operator import TestCalcu
import HTMLTestRunner
import unittest

def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCalc("test_calculate_sin"))
    suiteTest.addTest(TestCalc("test_calculate_cos"))
    suiteTest.addTest(TestCalc("test_clear"))
    suiteTest.addTest(TestCalc("test_backspace"))
    suiteTest.addTest(TestCalculator("test_get_digit"))
    suiteTest.addTest(TestCalcu("test_calculate_addition"))
    suiteTest.addTest(TestCalcu("test_subtraction"))
    suiteTest.addTest(TestCalcu("test_multiplication"))
    suiteTest.addTest(TestCalcu("test_divison"))
    suiteTest.addTest(TestCalcu("test_square_root"))
    suiteTest.addTest(TestCalcu("test_cube_root"))
    return suiteTest

if __name__=="__main__":
   filepath=r"C:\Users\u5550\Desktop\calculator_GUI\Calculator_HTML_Report.html"
   fp=open(filepath,'wb')
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'test1_report',description=u'Test report For calculator by SASHIT SHARMA')
   runner.run(Suite())
   fp.close()