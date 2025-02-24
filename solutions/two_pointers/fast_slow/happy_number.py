# https://leetcode.com/problems/happy-number/description/
# https://algo.monster/problems/happy_number

class Solution:    
    # if no loop, the number is a happy number
    def isHappy(self, n: int) -> bool:
        def computeSquare(a: int):
            num_strs = str(a)
            result = 0
            for num_str in num_strs:
                result += int(num_str) * int(num_str)
            return result
            
        slow_square = computeSquare(n)
        fast_square = computeSquare(slow_square) 
        
        while slow_square != 1 and fast_square != 1:
            slow_square = computeSquare(slow_square)
            fast_square = computeSquare(computeSquare(fast_square))
            if slow_square == fast_square: # To detect if the square computation lead to loop
                return False
            
        return True