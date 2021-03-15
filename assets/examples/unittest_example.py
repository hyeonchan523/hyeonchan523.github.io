import unittest
import check_module as check

class TestModule(unittest.TestCase):
    def setUp(self):
        self.year = 2001
    
    def tearDown(self):
        print('tearDown')
    
    def test_validity_check(self):
        expected = True
        answer = check.validity_check(self.year)
        self.assertEqual(answer, expected)
        
    def test_leap_year_check(self):
        expected = True
        answer = check.leap_year_check(self.year)
        self.assertEqual(answer, expected)
        
if __name__ == '__main__':
    unittest.main()