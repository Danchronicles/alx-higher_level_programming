import unittest
import myfile

class Testcalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(myfile.add(10, 5), 15)
        self.assertEqual(myfile.add(-1, 5), 0)
        self.assertEqual(myfile.add(-1, -1), -2)
        
if __name__ == '__main__':
    unittest.main()