# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?




# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#Answer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size_list = 0
        while temp is not None:
            temp = temp.next
            size_list+=1
        if size_list == 1:
            return None
        if size_list == n:
            return head.next
        dummy = curr = head
        if size_list > n:
            size_list = size_list - n

        count = 0
        while count<= size_list:
            if count == size_list-1:
                temp = curr
                curr.next = temp.next.next
                count+=1
            else:
                curr = curr.next
                count+=1
        return dummy