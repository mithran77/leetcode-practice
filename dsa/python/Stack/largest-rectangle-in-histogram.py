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
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            
            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        return maxArea
    
# Time & Space Complexity
# Time complexity: O(n ^ 2)
# Space complexity: O(1)

# Monotonic increasing stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while st and h < st[-1][1]:
                idx, height = st.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx

            st.append((start, h))

        for i, h in st:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)


if __name__ == '__main__':
    res = Solution()
    print(res.largestRectangleArea(heights = [2,1,5,6,2,3]))
    print(res.largestRectangleArea(heights = [2,4]))

