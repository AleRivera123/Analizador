from queue import Queue

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

def is_valid_math_expression(expression):

    if ' ' in expression:
        return False


    stack = Stack()
    previous_char = ""
    valid_chars = set("0123456789+-()")

    for i, char in enumerate(expression):

        if char not in valid_chars:
            return False


        if char == '(':
            if previous_char and previous_char in "0123456789)":
                return False
            stack.push(char)
        elif char == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
            if previous_char and previous_char in "+-(":
                return False


        if char in "+-":
            if previous_char == '' or previous_char in "+-(":
                return False
            if i + 1 < len(expression) and expression[i + 1] in "+-)":
                return False

        previous_char = char

    if not stack.is_empty():
        return False

    return True

expresiones = [
    "3+5-2",
    "3++5",
    "3+-5",
    "3+5-",
    "3+(5-2)",
    "3+5)-2",
    "3+5 - 2",
    "3+(5-2))",
    "3+(5-2",
    "(3+5)-2",
    "3(4-2)(5-2)"
]

for expr in expresiones:
    if is_valid_math_expression(expr):
        print(f"La expresión '{expr}' está bien escrita.")
    else:
        print(f"La expresión '{expr}' está mal escrita.")
