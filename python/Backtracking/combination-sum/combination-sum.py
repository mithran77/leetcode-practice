# https://leetcode.com/problems/combination-sum/description/
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # RCs
            # same
            cur.append(candidates[i])
            total += candidates[i]
            dfs(i, cur, total)
            # next
            cur.pop()
            total -= candidates[i]
            i += 1
            dfs(i, cur, total)

        dfs(0, [], 0)
        return res

if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum([2,3,6,7], 7))
    print(res.combinationSum([2,3,5], 8))
    print(res.combinationSum([2], 1))


# RTs
#
# [2, 3, 5], 8
#
# dfs(0, [], 0)
#
# dfs(0, [2], 2)
# dfs(0, [2, 2], 4)
#
# dfs(0, [2, 2, 2], 6)
# dfs(0, [2, 2, 2, 2], 8)
# dfs(1, [2, 2, 2], 6)
# dfs(1, [2, 2, 2, 3], 9)
# dfs(2, [2, 2, 2], 6)
# dfs(2, [2, 2, 2, 5], 11)
# dfs(3, [2, 2, 2], 6)
#
# dfs(1, [2, 2], 4)
#
# dfs(1, [2, 2, 3], 7)
# dfs(1, [2, 2, 3, 3], 10)
# dfs(2, [2, 2, 3], 7)
# dfs(2, [2, 2, 3, 5], 12)
# dfs(3, [2, 2, 3], 7)
#
# dfs(2, [2, 2], 4)
#
# dfs(2, [2, 2, 5], 9)
#
# dfs(3, [2, 2], 4)
#
# dfs(1, [2], 2)
# dfs(1, [2, 3], 5)
# dfs(1, [2, 3, 3], 8)
#
# dfs(2, [2, 3], 5)
# dfs(2, [2, 3, 5], 10)
#
# dfs(3, [2, 3], 5)
#
# dfs(2, [2], 2)
# dfs(2, [2, 5], 7)
# dfs(2, [2, 5, 5], 12)
#
# dfs(3, [2, 5], 7)
# dfs(3, [2], 2)
#
# dfs(1, [], 0)
#
# dfs(1, [3], 3)
# dfs(1, [3, 3], 6)
# dfs(1, [3, 3, 3], 9)
#
# dfs(2, [3, 3], 6)
# dfs(2, [3, 3, 5], 11)
#
# dfs(3, [3, 3], 6)
#
# dfs(2, [3], 3)
# dfs(2, [3, 5], 8)
#
# dfs(3, [3], 3)
#
# dfs(2, [], 0)
#
# dfs(2, [5], 5)
# dfs(2, [5, 5], 10)
#
# dfs(3, [5], 5)
#
# dfs(3, [], 0)