import unittest
from src.Math_Request import MathRequest
from src.Math_Lib import MathLib



class TestMathLib(unittest.TestCase):

    def setUp(self):
        pass

    def test_execute_add_get_result(self):
        #given
        math_request = MathRequest(3, '+', 4)

        #when
        MathLib.calculate(math_request)

        #then
        self.assertEqual(math_request.res, 7)

    def test_execute_sub_get_result(self):
        # given
        mathrequest = MathRequest(3, '-', 4)
        math_lib = MathLib(mathrequest)

        # when
        MathLib.calculate(mathrequest)

        # then
        self.assertEqual(mathrequest.get_res(), -1)

    def test_execute_mul_get_result(self):
        # given
        mathrequest = MathRequest(3, '*', 4)
        math_lib = MathLib(mathrequest)

        # when
        MathLib.calculate(mathrequest)

        # then
        self.assertEqual(mathrequest.get_res(), 12)

    def test_execute_div_get_result(self):
        # given
        mathrequest = MathRequest(3, '/', 4)
        math_lib = MathLib(mathrequest)

        # when
        MathLib.calculate(mathrequest)

        # then
        self.assertEqual(mathrequest.get_res(), 0.75)

    def test_execute_pow_get_result(self):
        # given
        mathrequest = MathRequest(3, '^', 81)
        math_lib = MathLib(mathrequest)

        # when
        MathLib.calculate(mathrequest)

        # then
        self.assertEqual(mathrequest.get_res(), )

    def test_execute_root_get_result(self):
        # given
        mathrequest = MathRequest(3, '**', 4)
        math_lib = MathLib(mathrequest)

        # when
        MathLib.calculate(mathrequest)

        # then
        self.assertEqual(mathrequest.get_res(), 1.32)

if __name__ == '__main__':
    unittest.main()