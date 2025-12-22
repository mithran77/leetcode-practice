# 300. Longest Increasing Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)

#         for i in range(len(nums) - 1, -1, -1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] < nums[j]:
#                     dp[i] = max(dp[i], 1 + dp[j])

#         return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums) # longest subsequence length ending at idx

        def rLengthOfLIS(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            result = 0
            for j in range(i): # While we compare against nums[i], we iterate till (i-1) 
                if nums[i] > nums[j]:
                    result = max(result, rLengthOfLIS(j))

            memo[i] = 1 + result
            return memo[i]

        result = 0
        for i in range(len(nums)):
            result = max(result, rLengthOfLIS(i))

        return result

if __name__ == '__main__':
    ans = Solution()
    # print(ans.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    print(ans.lengthOfLIS(nums = [0,1,0,3,2,3]))
    # print(ans.lengthOfLIS(nums = [7,7,7,7,7,7,7]))

