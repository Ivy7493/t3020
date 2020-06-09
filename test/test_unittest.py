import unittest
import os
import datamunger
this_dir = os.path.dirname(__file__)

class TestData(unittest.TestCase):
    
    def test_calctotalpass(self):
        TestNumbers = [360,10,20,30,40,50,60,70,80,90]
        result = datamunger.calc_total(TestNumbers)
        self.assertEqual(result,TestNumbers[0])

    def test_caltotalfail(self):
        TestNumbers = [360,10,20,450,40,50,60,70,80,90]
        result = datamunger.calc_total(TestNumbers)
        self.assertNotEqual(result,TestNumbers[0])

    def test_Testrowpass(self):
        curr = "440,20,30,40,50,60,70,80,90,100"
        currlist = curr.split(",")
        prev = [0,10,20,30,40,50,60,70,80,90]
        result = datamunger.check_row(1,prev,currlist)
        self.assertTrue(result)

    def test_Testrowfail(self):
        curr = "440,20,30,,50,60,70,80,90,100"
        currlist = curr.split(",")
        prev = [0,10,20,30,40,50,60,70,80,90]
        result = datamunger.check_row(1,prev,currlist)
        self.assertFalse(result)

    def test_Testmonotonicpass(self):
        prev = [0,10,20,30,40,50,60,70,80,90]
        curr = [10,20,30,40,50,60,70,80,90,100]
        result = datamunger.check_monotonic(prev,curr)
        self.assertTrue(result)

    def test_Testmonotonicfail(self):
        curr = [0,10,20,30,40,50,60,70,80,90]
        prev = [10,20,30,40,50,60,70,80,90,100]
        result = datamunger.check_monotonic(prev,curr)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
