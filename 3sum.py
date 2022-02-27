# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)        
        output = set()
        for k in range(len(s)):
            target = -s[k]
            i, j = k+1, len(s)-1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k],s[i],s[j]))
                    i += 1
                    j -= 1
        return output


if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))