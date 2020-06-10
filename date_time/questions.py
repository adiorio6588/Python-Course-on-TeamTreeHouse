class Questions:
    answers = None
    text = None

class Add(Questions):
    def __init__(self, num1, num2):
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2

class Multiply(Questions):
    def __init__(self, num1, num2):
        self.text = '{} x {}'.format(num1, num2)
        self.answer = num1 * num2