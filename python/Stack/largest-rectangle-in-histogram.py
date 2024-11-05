# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:

# Input: heights = [2,4]
# Output: 4

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

from typing import List

# Brute Force (expands from center)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            # max_area = max(max_area, heights[i])

            # l, r = max(0, i - 1), min(len(heights), i + 1)

            while l >= 0 and r < len(heights) :
                w = r - l + 1
                max_area = max(max_area, w * heights[i])
                if (-1 < l) and (heights[l] <= heights[i]):
                    l -= 1
                if r < len(heights) and (heights[r] <= heights[i]):
                    r += 1

        return max_area

if __name__ == '__main__':
    res = Solution()
    # print(res.largestRectangleArea(heights = [2,1,5,6,2,3]))
    print(res.largestRectangleArea(heights = [2,4]))

