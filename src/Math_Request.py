class MathRequest:

    def __init__ (self, ope1, oper, ope2,):
        self.ope1 = ope1
        self.oper = oper
        self.ope2 = ope2
        self.res = None

    def get_ope1(self):
        return self.ope1

    def get_oper(self):
        return self.oper

    def get_ope2(self):
        return self.ope2

    def set_res(self, value):
        self.res = value

    def to_string(self):
        return f"{self.ope1} {self.oper} {self.ope2} = {self.res}"

    @classmethod
    def verification_oper(self):
        valid_operators = ['add', 'sub', 'mul', 'div', 'paw', 'root']

        while True:
            oper = input("Enter an operator (add, sub, mul, div, paw, root): ").strip()

            if oper.lower() in valid_operators:
                return oper

            elif oper.lower() == "exit":
                print("Exiting...")
                return False

            else:
                print("Invalid operator. Please enter one of: add,sub,mul,div,paw,root")