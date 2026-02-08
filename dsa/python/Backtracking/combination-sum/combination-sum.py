# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.

# The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40


from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        results = []

        def backtrack(current_combo, current_sum, index):
            nonlocal results

            if current_sum > target:
                return

            if index == len(candidates):
                if current_sum == target:
                    results.append(current_combo.copy())
                return

            # Choose the current candidate (can reuse it)
            current_combo.append(candidates[index])
            backtrack(current_combo, current_sum + candidates[index], index)
            current_combo.pop()

            # Skip the current candidate
            backtrack(current_combo, current_sum, index + 1)

        backtrack([], 0, 0)
        return results

# Time:  O(2^t/m)
#    Total number of steps during the backtracking would be the number of
#    nodes in the tree
# Space: O(t/m)
#    Max size of cur
# Where t is the given target and m is the minimum value in nums


# Using template
# class Solution:
#     def combinationSum(
#         self, candidates: List[int], target: int
#     ) -> List[List[int]]:
#         combinations = []

#         def backtrack(cur, start, total):
#             if total == target:
#                 combinations.append(cur.copy())
#             if total >= target:
#                 return
#             for i in range(start, len(candidates)):
#                 cur.append(candidates[i])
#                 total += candidates[i]
#                 backtrack(cur, i, total)
#                 total -= candidates[i]
#                 cur.pop()

#         backtrack([], 0, 0)

#         return combinations


if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum([2, 3, 6, 7], 7))
    # print(res.combinationSum([2, 3, 5], 8))
    # print(res.combinationSum([2], 1))


# RTs
#
# [2, 3, 5], 8
#
# dfs(0, [], 0)
#
# dfs(0, [2], 2)
# dfs(0, [2, 2], 4)
#
# dfs(0, [2, 2, 2], 6)
# dfs(0, [2, 2, 2, 2], 8)
# dfs(1, [2, 2, 2], 6)
# dfs(1, [2, 2, 2, 3], 9)
# dfs(2, [2, 2, 2], 6)
# dfs(2, [2, 2, 2, 5], 11)
# dfs(3, [2, 2, 2], 6)
#
# dfs(1, [2, 2], 4)
#
# dfs(1, [2, 2, 3], 7)
# dfs(1, [2, 2, 3, 3], 10)
# dfs(2, [2, 2, 3], 7)
# dfs(2, [2, 2, 3, 5], 12)
# dfs(3, [2, 2, 3], 7)
#
# dfs(2, [2, 2], 4)
#
# dfs(2, [2, 2, 5], 9)
#
# dfs(3, [2, 2], 4)
#
# dfs(1, [2], 2)
# dfs(1, [2, 3], 5)
# dfs(1, [2, 3, 3], 8)
#
# dfs(2, [2, 3], 5)
# dfs(2, [2, 3, 5], 10)
#
# dfs(3, [2, 3], 5)
#
# dfs(2, [2], 2)
# dfs(2, [2, 5], 7)
# dfs(2, [2, 5, 5], 12)
#
# dfs(3, [2, 5], 7)
# dfs(3, [2], 2)
#
# dfs(1, [], 0)
#
# dfs(1, [3], 3)
# dfs(1, [3, 3], 6)
# dfs(1, [3, 3, 3], 9)
#
# dfs(2, [3, 3], 6)
# dfs(2, [3, 3, 5], 11)
#
# dfs(3, [3, 3], 6)
#
# dfs(2, [3], 3)
# dfs(2, [3, 5], 8)
#
# dfs(3, [3], 3)
#
# dfs(2, [], 0)
#
# dfs(2, [5], 5)
# dfs(2, [5, 5], 10)
#
# dfs(3, [5], 5)
#
# dfs(3, [], 0)
