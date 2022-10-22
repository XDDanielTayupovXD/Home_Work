from pydoc import plain


class Calculator:

    def calc_plus(num1, num2):
        print("Ответ:", num1 + num2)
    
    def calc_mines(num3, num4):
        print("Ответ:", num3 - num4)
    
    def calc_multiply(num5, num6):
        print("Ответ:", num5 * num6)
    
    def calc_divide(num7, num8):
        print("Ответ:", num7 % num8)

cals = Calculator()

Calculator.calc_plus(2, 7)
Calculator.calc_mines(17, 6)
Calculator.calc_multiply(6, 8)
Calculator.calc_divide(15, 4)
