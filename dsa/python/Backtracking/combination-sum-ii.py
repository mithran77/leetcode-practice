# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from typing import List

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res, cur = [], []
#         candidates.sort()

#         def backtrack(i, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
#             if total > target or i >= len(candidates):
#                 return

#             # PICK
#             total += candidates[i]
#             cur.append(candidates[i])
#             backtrack(i + 1, total)

#             # NO-PICK
#             while ((i + 1) < len(candidates) and candidates[i] == candidates[i + 1]):
#                 i += 1
#             total -= candidates[i]
#             cur.pop()
#             backtrack(i + 1, total)

#         backtrack(0, 0)

#         return res

# Time:  O(2^t/m)
    # Total number of steps during the backtracking would be the number of nodes in the tree
# Space: O(t/m)
    # Max size of cur
# Where t is the given target and m is the minimum value in nums


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(temp_list, start, total):
            if total == target:
                res.append(temp_list.copy())
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                temp_list.append(candidates[i])
                backtrack(temp_list, i + 1, total+candidates[i])
                temp_list.pop()
    
        backtrack([], 0, 0)

        return res

if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
    print(res.combinationSum2(candidates = [2,5,2,1,2], target = 5))

