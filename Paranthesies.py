# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Accepted
# 3.9M
# Submissions
# 9.7M
# Acceptance Rate
# 40.2%

# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in range(0,len(s)):
            if s[i] == '(' or  s[i] == '{' or  s[i] == '[':
                result.append(s[i])
            else:
                if len(result) == 0:
                    return False
                if s[i] == ')':
                    x = result.pop()
                    if x != '(' :
                        return False
                if s[i] == '}':
                    x = result.pop()
                    if x != '{':
                        return False                        
                if s[i] == ']':
                    x = result.pop()
                    if x != '[':
                        return False
        if(len(result) == 0):
            return True
        else:
            return False