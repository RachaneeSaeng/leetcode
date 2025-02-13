# https://leetcode.com/problems/basic-calculator/
class Solution:
     
    def calculate(self, s: str) -> int:
        
        def precedence(op: str) -> int:
            if op == '(' or op == ')':
                return 0
            elif op == '+' or op == '-':
                return 1
            else:
                return 2
            
        def apply_operator(a: int, op: str, b: int) -> int:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return a // b
                   
        nums, ops = [], []
        number = ''
        
        for char in s:            
            if char.isdigit():
                number += char
            else:
                if number:
                    nums.append(int(number))
                    number = ''
                    
                if char == '(':
                    ops.append(char)
                elif char == ')':
                    while (ops and ops[-1] != '('):
                        num2 = nums.pop()
                        num1 = nums.pop()
                        op = ops.pop()
                        nums.append(apply_operator(num1, op, num2))
                    ops.pop()
                elif char in '+-*/':
                    while (ops and ops[-1] != '(' and precedence(ops[-1]) >= precedence(char)):
                        num2 = nums.pop()
                        num1 = nums.pop()
                        op = ops.pop()
                        nums.append(apply_operator(num1, op, num2))
                    ops.append(char)
                    
        if number:
            nums.append(int(number))

        while (ops):
                num2 = nums.pop()
                num1 = nums.pop()
                op = ops.pop()
                nums.append(apply_operator(num1, op, num2))
                
        return nums[0]
    