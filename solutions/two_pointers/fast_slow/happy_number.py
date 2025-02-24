# https://leetcode.com/problems/happy-number/description/
# https://algo.monster/problems/happy_number

# time complexity: O(logn)
# space complexity: O(1)
# Note: this can be solved by using a hash table to store visited numbers but the space complexity will be O(logn)
class Solution:    
    # if no loop, the number is a happy number
    def isHappy(self, n: int) -> bool:
        def computeSquare(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow = n
        fast = computeSquare(n)
        
        while fast != 1 and slow != fast:
            slow = computeSquare(slow)
            fast = computeSquare(computeSquare(fast))
            
        return fast == 1