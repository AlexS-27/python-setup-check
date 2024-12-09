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
        return f"{self.ope1} {self.oper} {self.ope2} {self.res}"

