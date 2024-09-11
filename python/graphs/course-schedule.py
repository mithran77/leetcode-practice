# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have 
# finished course 1. So it is impossible.

# Constraints:

# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
from typing import List
import collections


# class Solution:

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         dependentCourses = [[] for _ in range(numCourses)] # Directed graph- adjacency list
#         prereqCnt = [0 for  _ in range(numCourses)] # InDegree
#         for course,itsPrereq in prerequisites:
#             dependentCourses[itsPrereq].append(course)
#             prereqCnt[course]+=1

#         prereqCompletedCnt = 0 # Cnt of courses whose prerequisite_courses are completed
#         # Cnt of vertices with inDegree zero

#         prereqCompletedOf = collections.deque()
#         for course in range(numCourses): # Loop to add courses as completed if they have no dependents
#             if prereqCnt[course] == 0:
#                 prereqCompletedOf.append(course)
#                 prereqCompletedCnt += 1

#         while prereqCompletedOf:
#             prereqCourse = prereqCompletedOf.popleft()
#             # Now decrement count-of-Incomplete-prerequisites for all those courses 
#             #          for which curr_course was one of the prerequisite
#             for course in dependentCourses[prereqCourse]:
#                 prereqCnt[course] -= 1
#                 if prereqCnt[course] == 0:
#                     prereqCompletedCnt += 1
#                     prereqCompletedOf.append(course)

#         return prereqCompletedCnt == numCourses


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsReq = { i : [] for i in range(numCourses) }
        visited = set()

        for crs, req in prerequisites:
            crsReq[crs].append(req)

        def dfs(crs):
            # BCs
            if crs in visited: # Cycle
                return False
            if crsReq[crs] == []:
                return True

            visited.add(crs)
            # RCs
            for req in crsReq[crs]:
                if not dfs(req):
                    return False

            visited.remove(crs)
            crsReq[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


if __name__ == '__main__':
    res = Solution()
    print(res.canFinish(2, [[1,0]]))

