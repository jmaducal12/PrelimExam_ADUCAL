import unittest

def check(x):

    return x == "MIGUEL"

class myTest(unittest.TestCase):

    def test (self): 

        self.assertTrue(check("ADUCAL"))

if __name__ == '__main__':

    unittest.main()