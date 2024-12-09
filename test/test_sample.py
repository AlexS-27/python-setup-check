import unittest
from src.MathRequest import MathRequest
from src.MathLib import MathLib

class TestMathRequest(unittest.TestCase):

    def setUp(self):
        self.ope1 = 3
        self.oper = "+"
        self.ope2 = 5
        self.res = 8
        self.mathRequest = MathRequest(self.ope1, self.oper, self.ope2, self.res)


    def test_get_ope(self):
        self.assertEqual(self.mathRequest.get_ope1(), self.ope1)

    def test_get_oper(self):
        self.assertEqual(self.mathRequest.get_oper(), self.oper)

    def test_get_ope2(self):
        self.assertEqual(self.mathRequest.get_ope2(), self.ope2)

    def test_get_res(self):
        self.assertEqual(self.mathRequest.get_res(), self.res)

    def test_set_res(self):
        self.assertEqual(self.mathRequest.set_res(), self.res)

    def test_to_string(self):
        self.assertEqual(self.mathRequest.to_string(), self.mathRequest.to_string())

if __name__ == '__main__':
    unittest.main()