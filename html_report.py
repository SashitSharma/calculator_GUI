import unittest
from HTMLTestRunner import HTMLTestRunner
from test_calculator import TestCalc
from test_get_digit import TestCalculator
from test_operator import TestCalcu


aTest_Classes_To_Run = [TestCalc, TestCalcu, TestCalculator]
aTest_Suite_List = []
aTest_Loader = unittest.TestLoader()

for aTest_Class in aTest_Classes_To_Run:
    aTest_Suite = aTest_Loader.loadTestsFromTestCase(aTest_Class)
    aTest_Suite_List.append(aTest_Suite)

aUnittest_Test_Suite = unittest.TestSuite(aTest_Suite_List)

aTestRunner = HTMLTestRunner()

aTestRunner.run(aUnittest_Test_Suite)

if __name__ == "__main__":
    report_file = open('test_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, verbosity=2, description='Test Report', title='Calculator Tests')
    unittest.main(testRunner=runner)
    report_file.close()