from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operaters = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operaters:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    result = operand1 + operand2
                    stack.append(result)

                elif token == "-":
                    result = operand1 - operand2
                    stack.append(result)
                    
                elif token == "*":
                    result = operand1 * operand2
                    stack.append(result)

                elif token == "/":
                    result = int(operand1 / operand2)
                    stack.append(result)

            else:
                stack.append(int(token))

        return stack.pop()