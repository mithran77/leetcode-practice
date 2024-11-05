# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that 
# answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

from typing import List

# # brute force
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(temperatures)):
#             days = 0
#             for j in range(i + 1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     days = j - i
#                     break
#             ans.append(days)

#         return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack_i = stack.pop()
                ans[stack_i] = (i - stack_i)

            stack.append(i)

        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
    print(res.dailyTemperatures(temperatures = [30,40,50,60]))
    print(res.dailyTemperatures(temperatures = [30,60,90]))

