# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the
# longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

# class Solution:

#     def longestConsecutive(self, nums: List[int]) -> int:

#         snums = sorted(list(set(nums)))
#         if len(snums) == 1:
#             return 1

#         cnt, tmp_cnt = 0, 1

#         for i in range(len(snums)-1):
#             if snums[i] + 1 == snums[i+1]:
#                 tmp_cnt += 1
#             else:
#                 tmp_cnt = 1
#             cnt = max(cnt, tmp_cnt)

#         return cnt


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in snums:
                length = 0
                while (n + length) in snums:
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    res = Solution()
    print(res.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(res.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(res.longestConsecutive([1, 2, 0, 1]))
    print(res.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(res.longestConsecutive([0, 0]))
