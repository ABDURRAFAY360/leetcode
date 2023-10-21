# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# https://leetcode.com/problems/longest-common-prefix/description/?source=submission-ac

#Solution 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        result = ""
        for i in range(1,len(strs)):
            if len(shortest) > len(strs[i]):
                shortest = strs[i]
                track = i
        for i in range(0,len(shortest)):
            count = 0
            for y in range(0,len(strs)):
                if(shortest[i] == strs[y][i]):
                    count=count+1
            if(count == len(strs)):
                result+=shortest[i]
            else:
                break
        return result