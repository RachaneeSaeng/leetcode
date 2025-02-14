# https://leetcode.com/problems/valid-parentheses/

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = {'()', '{}', '[]'}
        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack or stack.pop() + char not in valid_pairs:
                return False

        return not stack