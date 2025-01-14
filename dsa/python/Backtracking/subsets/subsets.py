# 78. Subsets

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

from typing import List

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         powerset = []

#         def dfs(cur, i):
#             if i >= len(nums):
#                 powerset.append(cur.copy())
#                 return
#             # Pick
#             cur.append(nums[i])
#             dfs(cur, i + 1)
#             # No pick
#             cur.pop()
#             dfs(cur, i + 1)

#         dfs([], 0)

#         return powerset

# Time: O(2^n * n)
    # 2^n subsets
    # In worst case, can be of length n
# Space: O(n)
    # cur grows to length n
    # Auxiliary stack space also can grow to n

# Using template
# https://leetcode.com/problems/subsets/solutions/27281/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []

        def backtrack(cur, start):
            powerset.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)
        return powerset

# RT [1,2,3]
# backtrack([], 0)          [[]]
# backtrack([1], 1)         [[], [1]]
# backtrack([1, 2], 2)      [[], [1], [1, 2]]
# backtrack([1, 2, 3], 3)   [[], [1], [1, 2], [1, 2, 3]]
# --------------BACKTRACK------------  x2
# backtrack([1, 3], 3)      [[], [1], [1, 2], [1, 2, 3], [1, 3]]
# --------------BACKTRACK------------  x2
# backtrack([2], 2)      [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
# backtrack([2, 3], 3)      [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
# --------------BACKTRACK------------  x2
# backtrack([3], 3)      [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# --------------BACKTRACK------------  x2


# RT [0]
# backtrack([], 0)      [[]]
# backtrack([0], 1)     [[], [0]]

if __name__ == '__main__':
    res = Solution()
    print(res.subsets(nums = [1,2,3]))
    # print(res.subsets(nums = [0]))

