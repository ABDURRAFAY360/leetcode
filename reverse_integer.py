# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1


# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*-1  # Simplify negation by using the unary operator

            # Convert x to a string, reverse it, and add '-' at the beginning

            reversed_str = '-' + str(x)[::-1]

            # Convert the reversed string back to an integer
            reversed_x = int(reversed_str)

            # Check for overflow, as specified in the problem
            if reversed_x < -2**31:
                return 0
            return reversed_x
        else:
            # Convert x to a string, reverse it
            reversed_str = str(x)[::-1]

            # Convert the reversed string back to an integer
            reversed_x = int(reversed_str)

            # Check for overflow, as specified in the problem
            if reversed_x > 2**31 - 1:
                return 0
            return reversed_x
