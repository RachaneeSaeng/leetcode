# https://leetcode.com/problems/valid-palindrome/
# https://algo.monster/problems/valid_palindrome

from curses.ascii import isalnum

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        def isEqualIgnoreCase(x: str, y: str):
            return x.casefold() == y.casefold()
        
        i,j = 0,len(s)-1
        while i < j:            
            if isalnum(s[i]) and isalnum(s[j]):
                if not isEqualIgnoreCase(s[i], s[j]):
                    return False
                i += 1
                j -=1
            elif not isalnum(s[i]):
                i += 1
            else:
                j -=1 
        return True
        