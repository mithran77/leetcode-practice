# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Practice
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def traverseList(self):
#         # Base case
#         if not self.head: return []

#         vals = []
#         tmp = self.head

#         while tmp.next is not None:
#             vals.append(tmp.val)
#             tmp = tmp.next

#         vals.append(tmp.val)

#         return vals

# # class Solution:
# #     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# #         pass

# if '__main__' == __name__:

#     head = [1,2,3,4,5]


#     ll = LinkedList()

#     # Add elements to linked list
#     for i, val in enumerate(head):
#         if i == 0:
#             ll.head = ListNode(val)
#         else:
#             tmp = ll.head
#             while tmp.next != None:
#                 tmp = tmp.next
#             tmp.next = ListNode(val)

#     print(ll.traverseList())
#     # data = ll.traverseList()
#     # Reverse linked list
#     # for i in range(len(data)-1 , -1, -1):

#     # Add elements to linked list
#     for i in range(len(head) - 1 , -1, -1):
#         if i == len(head) - 1:
#             ll.head = ListNode(head[i])
#         else:
#             tmp = ll.head
#             while tmp.next != None:
#                 tmp = tmp.next
#             tmp.next = ListNode(head[i])

#     print(ll.traverseList())

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr_node = head
        prev_node = None

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))
