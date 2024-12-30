# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# Input: head = [1,2]
# Output: false

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Go to middle of list
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next

        # Reverse 2nd half of list
        
        p = None
        c = s
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        
        l1, l2 = head, p
        
        while l1 and l2:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        # if l2:
        #     return False
        # If there is a last element, it is def the middle element

        return True

if __name__ == '__main__':
    res = Solution()
    print(res.isPalindrome(head = [1,2,2,1]))
    print(res.isPalindrome(head = [1,2]))

