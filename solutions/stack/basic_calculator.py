# https://leetcode.com/problems/basic-calculator/
class Solution: 
    def calculate(self, s: str) -> int:
        stack = []
        result, sign, number = 0, '+', ''
        
        for char in s:            
            if char.isdigit():
                number += char
            else:
                if number:
                    result = Solution.updateResult(result, sign, int(number))
                    number = ''
                    
                if char in '+-*/':
                    sign = char
                elif char == '(':
                    stack.append(result)
                    stack.append(sign)
                    result, sign = 0, '+'
                elif char == ')':
                    sing = stack.pop()    
                    result = Solution.updateResult(stack.pop(), sing, result)
                    
        if number:
            result = Solution.updateResult(result, sign, int(number))

        return result
    
    @staticmethod
    def updateResult(currentValue: int, sign: str, number: int) -> int:
        if sign == '+':
            return currentValue + number
        elif sign == '-':
            return currentValue - number
        elif sign == '*':
            return currentValue * number
        elif sign == '/':
            return currentValue // number
    
    