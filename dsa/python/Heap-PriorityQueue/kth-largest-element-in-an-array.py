# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

from typing import List
from heapq import heapify, heappop

# preddy
# max heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [ (-1 * n) for n in nums ] # O(n)
        heapify(max_heap) # O(n)

        while k > 1: # O(k-1)
            heappop(max_heap) # O(log n)
            k -= 1

        return (-1 * heappop(max_heap)) # O(log(n-k))

if __name__ == '__main__':
    ans = Solution()
    print(ans.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    print(ans.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

# Time: O(n)
# Space: O(n)