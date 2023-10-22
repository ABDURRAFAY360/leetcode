# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# ANSWER

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
        '2': "ABC",
        '3': "DEF",
        '4': "GHI",
        '5': "JKL",
        '6': "MNO",
        '7': "PQRS",
        '8': "TUV",
        '9': "WXYZ",
        '1': "1",
        '0': "0"
        }
        s=""
        str_list = []
        def get_all_compination(mapping,digits,i,s,str_list):
            if i == len(digits):
                str_list.append(s.lower())
                return
            for c in mapping[digits[i]]:
                get_all_compination(mapping,digits,i+1,s+c,str_list)
            return str_list
        result = get_all_compination(mapping,digits,0,s,str_list)
        return result