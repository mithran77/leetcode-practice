# https://leetcode.com/problems/interval-list-intersections/solution/

# Here is your problem! 

# Given two lists of time intervals, find the intersection of these two lists. 
# Each list consists of disjoint intervals sorted based on their start time. 
# Please solve this on O(n) time complexity. Please submit your approaches and pseudocode to me. :)


# Example 1:


# Each tuple is a time interval [t1, t2] where t1 is the start time and t2 is the end time.


# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]

# Output: [2, 3], [5, 6], [7, 7]


# Explanation: The output list contains the common intervals between the two lists.


# Example 2:


# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]

# Output: [5, 7], [9, 10]

# Explanation: The output list contains the common intervals between the two lists.
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []

        while i < len(firstList) and j < len(secondList):
            si = max(firstList[i][0], secondList[j][0])
            ei = min(firstList[i][1], secondList[j][1])
            if si <= ei:
                ans.append([si, ei])
            
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1


        return ans

if '__main__' == __name__:
    ans = Solution()
    res = ans.intersectionIntervals([()])
    print(res)



# class Solution:
#     def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
#         ans = []
#         i = j = 0

#         while i < len(A) and j < len(B):
#             # Let's check if A[i] intersects B[j].
#             # lo - the startpoint of the intersection
#             # hi - the endpoint of the intersection
#             lo = max(A[i][0], B[j][0])
#             hi = min(A[i][1], B[j][1])
#             if lo <= hi:
#                 ans.append([lo, hi])

#             # Remove the interval with the smallest endpoint
#             if A[i][1] < B[j][1]:
#                 i += 1
#             else:
#                 j += 1

#         return ans