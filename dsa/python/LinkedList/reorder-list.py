# https://leetcode.com/problems/reorder-list/description/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         cur, nums = head, []
#         while cur:
#             nums.append(cur.val)
#             cur = cur.next

#         l, r = 0, len(nums) - 1
#         cur = head
#         while l < r:
#             cur.val = nums[l]
#             cur = cur.next
#             cur.val = nums[r]
#             cur = cur.next
#             l, r = l + 1, r + 1

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next

        # Find mid point
        while f and f.next:
            s = s.next
            f = f.next.next

        # Reverse 2nd half
        cur = s.next
        prev = s.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # Merge 2 halfs
        l1, l2 = head, prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2

if __name__ == '__main__':
    res = Solution()
    print(res.reorderList([1,2,3,4]))

