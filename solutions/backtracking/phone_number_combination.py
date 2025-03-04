# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List

# Time complexity: O(3^n * 4^m) -- where n is the number of digits that have 3 letters and m is the number of digits that have 4 letters
# Space complexity: O(3^n * 4^m)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        n = len(digits)

        def backtrack(start, combination):
            if start == n: # got a combination to add to the result when combination has all digits's letters
                result.append(''.join(combination))
                return

            for letter in phone[digits[start]]:
                combination.append(letter) # append current a letter of the current digit
                backtrack(start + 1, combination) # go to next digit to append letters of that digit
                combination.pop()

        backtrack(0, [])
        return result