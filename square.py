import unittest

def perimeter(sides):
    
    return 4*sides

def area(side):

    return side*side

class square(unittest.TestCase):

    def perimetertest (self): 

        self.assertEqual(perimeter(4),16)

    def areatest (self): 

        self.assertEqual(area(5),20)

if __name__ == '__main__':

    unittest.main()



