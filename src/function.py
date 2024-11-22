from main import main

def ask_user_input():

    global operand1
    # Get first operand from the user
    operand1 = float(input("Enter the first operand: "))

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    global operand2
    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))

    return operand1, operator, operand2

def calculate(ope1, oper, ope2):
    # Perform the operation based on the operator
    res = None
    match operator:
        case '+':
            res = (operand1 + operand2)

        case '-':
            res = (operand1 - operand2)

        case '*':
            res = (operand1 * operand2)

        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = (ope1 / ope2)

        case _:
            print("Error: Operator '{}' not recognized.".format(operator))
            return

    return res

def display_result(ope1, oper, ope2, res):
    print(f"{ope1} {oper} {ope2}={res}")



