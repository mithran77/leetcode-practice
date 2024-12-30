# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return 
# the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# [[1,2],[2,3],[1,3],[3,4]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104
from typing import List


# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

#         # Base case (Lower boundary)
#         if len(intervals) <= 1:
#             return 0

#         # Sort Intervals based on first element
#         intervals.sort(key=lambda x: x[0])

#         count = 0
#         sp, fp = 0, 1

#         while fp < len(intervals):

#             end1 = intervals[sp][0]
#             start2 = intervals[fp][0]

#             while sp < fp:

#                 if start2 < end1:
#                     intervals.pop(fp)
#                     count += 1
#                 else:
#                     sp += 1

#             fp += 1
        
#         return count

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        res, prevEnd = 0, intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prevEnd: # overlapping
                prevEnd = min(prevEnd, end)
                res += 1
            else:
                prevEnd = end

        return res

if __name__ == '__main__':
    ans = Solution()
    print(ans.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
    print(ans.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
    print(ans.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))

