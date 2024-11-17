# 25. Reverse Nodes in k-Group

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy initialization
        prev = dummy = ListNode(0, head)
        s, f = head, head
        i = 1

        # Split nodes into k sized groups
        while f:

            if (i % k == 0):

                # Sever
                tmp = f.next
                f.next = None
                f = tmp

                # Reverse
                new_head = self.reverse(s)

                # Correct link
                prev.next = new_head

                # Assign new prev & move s
                prev = s
                s = f

            else:
                f = f.next

            i += 1

        # Optionally add last group
        if s:
            prev.next = s

        return dummy.next

    def reverse(self, head):
        # Reverse and return new head
        p, c = None, head

        while c:
            t = c.next
            c.next = p
            p = c
            c = t

        return p


if __name__ == '__main__':
    res = Solution()

