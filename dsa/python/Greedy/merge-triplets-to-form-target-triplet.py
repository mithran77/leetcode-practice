# 1899. Merge Triplets to Form Target Triplet

# Hint
# A triplet is an array of three integers. You are given a 2D integer array triplets,
# where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z]
# that describes the triplet you want to obtain.

# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
# Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.


# Example 1:
# Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5].
# triplets = [[2,5,3],[1,8,4],[2,7,5]]
# The target triplet [2,7,5] is now an element of triplets.

# Example 2:
# Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
# Output: false
# Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

# Example 3:
# Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]].
# Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
# - Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
# Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
# The target triplet [5,5,5] is now an element of triplets.


# Constraints:
# 1 <= triplets.length <= 105
# triplets[i].length == target.length == 3
# 1 <= ai, bi, ci, x, y, z <= 1000


from typing import List
from collections import deque, Counter

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            for j in range(3):
                if triplets[i][j] == target[j]:
                    res.add(j)

        return len(res) == 3


if __name__ == '__main__':
    res = Solution()
    print(res.mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]))
    print(res.mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))
    print(res.mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))


