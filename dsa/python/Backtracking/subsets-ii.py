# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            if i > len(nums) or len(cur) > len(nums):
                return

            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

            # Move i till it is going to be unique
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return res

# Time  : O(n log n * 2^n * n)
# Space : O(n)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(temp_list, start):
            res.append(temp_list.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp_list.append(nums[i])
                backtrack(temp_list, i + 1)
                temp_list.pop()

        backtrack([], 0)

        return res


if __name__ == '__main__':
    res = Solution()
    print(res.subsetsWithDup(nums = [1,2,2]))
    print(res.subsetsWithDup(nums = [0]))


