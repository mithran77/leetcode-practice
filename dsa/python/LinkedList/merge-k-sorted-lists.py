# https://leetcode.com/problems/merge-k-sorted-lists/description/
# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))

            lists = merged

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next

if __name__ == '__main__':
    res = Solution()

