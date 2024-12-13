from src.Math_Request import MathRequest
import math

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

        match oper:
            case 'add':
                res = ope1 + ope2
                math_request.set_res(res)

            case 'sub':
                res = ope1 - ope2
                math_request.set_res(res)

            case 'mul':
                res = ope1 * ope2
                math_request.set_res(res)

            case 'div':
                if ope2 == 0:
                    print("error it's not possible to divide by zero")
                    return
                res = ope1 / ope2
                math_request.set_res(res)

            case 'paw':
                res = ope1 ** ope2
                math_request.set_res(res)

            case 'root':
                if ope2 == 0:
                    raise ValueError("L'indice de la racine (ope2) ne peut pas être zéro.")
                elif ope1 < 0 and ope2 % 2 == 0:
                    raise ValueError("Impossible de calculer une racine paire d'un nombre négatif.")
                else:
                    res = round(ope1 ** (1 / ope2),2)
                    math_request.set_res(res)

            case _:
                print("Error: Operator '{}' not recognized.".format(oper))
                return

        return math_request.set_res(res)




    def verification_oper(self):
        valid_operators = ['+', '-', '*', '/', '^']

        while self.math_request.oper not in valid_operators:
            print("Invalid operator. Please enter one of: +,-,*,/,^")
            new_oper = self.math_request.oper()

            if new_oper.lower() == "exit":
                print("Exiting...")
                return False

            self.math_request.oper = new_oper

        return True

