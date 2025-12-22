# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.

# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is
# connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:

#         curr_node = head
#         id_list = [id(head)]

#         while curr_node is not None:
#             if id(curr_node.next) in id_list:
#                 return True
#             else:
#                 curr_node = curr_node.next
#                 id_list.append(id(curr_node))

#         return False

# Floyd cycle detection algorithm

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:

#         ptr1 = head
#         if head is not None: 
#             ptr2 = head.next

#         while ptr1 is not None:

#             if ptr2 is None or ptr2.next is None:
#                 break
#             else:
#                 if ptr1 == ptr2:
#                     return True
#                 ptr2 = ptr2.next.next
#             ptr1 = ptr1.next

#         return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True

        return False


if __name__ == '__main__':
    res = Solution()
    print()
