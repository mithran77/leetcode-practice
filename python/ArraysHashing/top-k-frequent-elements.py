# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         n_count = {}

#         for n in nums:
#             if n in n_count:
#                 n_count[n] += 1
#             else:
#                 n_count[n] = 1

#         output = []
#         for _ in range(k):
#             max = next(iter(n_count))
#             for k in n_count:
#                 if n_count[k] > n_count[max]:
#                     max = k
#             output.append(max)
#             del n_count[max]
        
#         return output

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        res = []
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    ans = Solution()
    print(ans.topKFrequent([1,1,1,2,2,3], 2))
