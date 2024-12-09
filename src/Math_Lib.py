from src.Math_Request import MathRequest

class MathLib:

    def __init__(self, math_request, res=0):
        if not isinstance(math_request, object): #check if MathRequest is a isinstance
            raise TypeError('MathLib constructor must be of type MathRequest')

        self.math_request = math_request
        self.res = res

    @classmethod
    def calculate(self, math_request):
        # Perform the operation based on the operator
        ope1 = math_request.get_ope1()
        oper = math_request.get_oper()
        ope2 = math_request.get_ope2()

        if oper == '+':
            res = ope1 + ope2
            math_request.set_res(res)

        if oper == '-':
            res = ope1 - ope2
            math_request.set_res(res)

        if oper == '*':
            res = ope1 * ope2
            math_request.set_res(res)




    def verification_oper(self):
        valid_operators = ['+', '-', '*', '/', '^']

        while self.math_request.oper not in valid_operators:
            print("Invalid operator. Please enter one of: +,-,*,/,^")
            new_oper = self.math_request.get_oper()

            if new_oper.lower() == "exit":
                print("Exiting...")
                return False

            self.math_request.oper = new_oper

        return True

    def get_res(self):
        return self.res