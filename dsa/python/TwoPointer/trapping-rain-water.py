# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import List

# # 2P
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         max_left, max_right, min_max = \
#             [0] * len(height), [0] * len(height), [0] * len(height)

#         # Left max
#         prev_max = 0
#         for i in range(len(height)):
#             max_left[i] = prev_max
#             prev_max = max(prev_max, height[i])

#         # Right max
#         prev_max = 0
#         for i in range(len(height) - 1, -1, -1):
#             max_right[i] = prev_max
#             prev_max = max(prev_max, height[i])

#         # Min Max
#         for i in range(len(height)):
#             min_max[i] = min(max_left[i], max_right[i])

#         # Calculate trapped water
#         trapped_water = 0
#         for i in range(len(height)):
#             water = min_max[i] - height[i]
#             if water > 0:
#                 trapped_water += water

#         return trapped_water


# 2P Space Optimized
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped_water = 0
        max_left, max_right = height[l], height[r]

        while l <= r:
            if max_left < max_right:
                water = max_left - height[l]
                if water > 0:
                    trapped_water += water

                max_left = max(max_left, height[l])
                l += 1

            else:
                water = max_right - height[r]
                if water > 0:
                    trapped_water += water

                max_right = max(max_right, height[r])
                r -= 1

        return trapped_water


if __name__ == '__main__':
    res = Solution()
    print(res.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    print(res.trap(height = [4,2,0,3,2,5]))


