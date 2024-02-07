# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array 
# of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Sort on first element
#         intervals = sorted(intervals, key=lambda x: x[0])
#         output = [intervals[0]]


#         for lower, upper in intervals:
#             existing_upper = output[-1][1]
#             if existing_upper >= lower:
#                 output[-1][1] = max(upper, existing_upper)
#             else:
#                 output.append([lower, upper])

#         return output


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Base case
        if len(intervals) < 2:
            return intervals

        # sort on first value
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0

        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                if intervals[i][1] >= intervals[i+1][1]:
                    del(intervals[i+1])
            else:
                i += 1

        return intervals


if __name__ == '__main__':
    res = Solution()
    print(res.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(res.merge([[1,4],[4,5]]))