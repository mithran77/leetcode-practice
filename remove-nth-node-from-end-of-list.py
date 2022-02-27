# 19. Remove Nth Node From End of List

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Took too long
# from typing import Optional


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         # Base cases
#         if not head or (head.next is None and n == 1):
#             return None

#         # Find length of linked list
#         curr_node = head
#         ll_len = 0

#         while curr_node:
#             ll_len += 1
#             curr_node = curr_node.next

#         # Base case n == len of list, delete head
#         if ll_len == n:
#             return head.next

#         target_node = ll_len - n
#         curr_node = head
#         count = 0

#         while count >= 0:
#             curr_node
#             count += 1


#         for _ in range(target_node - 1):
#             curr_node = curr_node.next
        
#         if curr_node and curr_node.next:
#             curr_node.next = curr_node.next.next
#         else:
#             head = None

#         return head

# if __name__ == '__main__':
#     ans = Solution()
#     print(ans.removeNthFromEnd())

# [1,2]
# 2

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = s = head

        for i in range(n):
            if f.next is None:
                # Base case for n == len of list, delete head
                if i == n-1:
                    head = head.next
                return head
            f = f.next

        while f.next:
            s = s.next
            f = f.next

        if s.next:
            s.next = s.next.next

        return head


if __name__ == '__main__':
    ans = Solution()
    print(ans.removeNthFromEnd())

# [1,2]
# 2