# 11. Container With Most Water
#
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and 
# (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the 
# container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# brute-force
from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         answer = 0
#         for i in range(0, len(height) - 1):
#             for j in range(i + 1, len(height)):
#                 area = (j - i) * min(height[i], height[j])
#                 if area > answer:
#                     answer = area

#         return answer

# if __name__ == '__main__':
#     res = Solution()
#     print(res.maxArea([1,1]))


# 2 pointer

# class Solution:
#     def maxArea(self, height: List[int]) -> int:

#         slow_pointer, fast_pointer, answer = 0, (len(height) - 1), 0

#         while slow_pointer < fast_pointer:
#             area = (fast_pointer - slow_pointer) * min(height[slow_pointer], height[fast_pointer])
#             if (area > answer):
#                 answer = area

#             if height[slow_pointer] < height[fast_pointer]:
#                 slow_pointer += 1
#             else:
#                 fast_pointer -= 1

#         return answer

# One thing that is ignored in the explanation is the h[i] == h[j] case.
# You need to prove that in this case, it does not matter whether you perform i++ or j--,
# because if h[i] == h[j], neither (i+1, j) or (i, j-1) can be potential solutions because
# the area obtained is necessarily smaller than (i, j).

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0

        while l < r:
            min_height = min(height[l], height[r])
            cur_area = min_height * (r - l)
            max_area = max(max_area, cur_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,8,6,2,5,4,8,3,7]))
    print(res.maxArea([1,1]))

