# 46. Permutations

# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from typing import List


# # Recursive
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if nums == []:
#             return [[]]

#         perms = self.permute(nums[1:])

#         res = []
#         for p in perms:  # O(n!)
#             for i in range(len(p) + 1):  # O(n)
#                 p_copy = p.copy()
#                 p_copy.insert(i, nums[0])  # O(n)
#                 res.append(p_copy)

#         return res


# RT
# nums = [1, 2, 3]
# permute([1, 2, 3]) res = []
# permute([2, 3]) res = []
# permute([3]) res = []
# permute([]) res = [[]]
# permute([3]) res = [[3]]
# permute([2, 3]) res = [[2, 3], [3, 2]]
# permute([1, 2, 3]) res = [
# [1, 2, 3], [2, 1, 3], [2, 3, 1],
# [1, 3, 2], [3, 1, 2], [3, 2, 1]
# ]

# Time: O(n! * n^2)
# number of perms O(n!)
# Insertion into specified element of list O(n)
# Done for each element O(n)

# Space: O(n! * n)
# We have n! permutations O(n!)
# We maintain copies of permuatations for each element in nums O(n)


# Backtracking
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(curr):
#             if len(curr) == len(nums):
#                 ans.append(curr.copy())
#                 return

#             for num in nums:
#                 if num not in curr:
#                     curr.append(num)
#                     backtrack(curr)
#                     curr.pop()

#         ans = []
#         backtrack([])
#         return ans


# Time: O(n * n!)
# Space: O(n)
# Call stack is O(n)
# cur is shared across the call stacks O(n)


# # Using template
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def backtrack(tmp_list):
#             if len(tmp_list) == len(nums):
#                 res.append(tmp_list.copy())
#             if len(tmp_list) > len(nums):
#                 return
#             for i in range(len(nums)):
#                 if nums[i] not in tmp_list:
#                     tmp_list.append(nums[i])
#                     backtrack(tmp_list)
#                     tmp_list.pop()

#         backtrack([])
#         return res


# # Boolean list
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         permutations = []

#         def backtrack(current_perm, used):
#             nonlocal permutations

#             if len(current_perm) == len(nums):
#                 permutations.append(current_perm.copy())
#                 return

#             for idx in range(len(nums)):
#                 if not used[idx]:
#                     used[idx] = True
#                     current_perm.append(nums[idx])
#                     backtrack(current_perm, used)
#                     current_perm.pop()
#                     used[idx] = False

#         backtrack([], [False] * len(nums))
#         return permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(current_perm, mask):
            nonlocal permutations

            if len(current_perm) == len(nums):
                permutations.append(current_perm.copy())
                return

            for idx in range(len(nums)):
                if not (mask & (1 << idx)):
                    current_perm.append(nums[idx])
                    backtrack(current_perm, mask | (1 << idx))
                    current_perm.pop()

        backtrack([], 0)
        return permutations


if __name__ == "__main__":
    res = Solution()
    print(res.permute(nums=[1, 2, 3]))
    print(res.permute(nums=[0, 1]))
