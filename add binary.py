# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        def convertToDecimal(num):
            result = 0
            power = len(num)-1
            for i in num:
                result+=int(i)* 2**power
                power-=1
            return result
        d_a = convertToDecimal(a)
        d_b = convertToDecimal(b)
        result = d_a + d_b
        if (result == 0):
            return "0"
        final_result = ""
        while result >0:
            final_result+= str(result % 2)
            result = result // 2
        return final_result[::-1]




