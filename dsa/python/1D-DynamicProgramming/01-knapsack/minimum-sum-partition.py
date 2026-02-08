# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1
# Minimum sum partition

# Given an array arr[]  containing non-negative integers, the
# task is to divide it into two sets set1 and set2 such that
# the absolute difference between their sums is minimum and
# find the minimum difference.

# Examples:

# Input: arr[] = [1, 6, 11, 5]
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11
# Hence, minimum difference is 1.

# Input: arr[] = [1, 4]
# Output: 3
# Explanation:
# Subset1 = {1}, sum of Subset1 = 1
# Subset2 = {4}, sum of Subset2 = 4
# Hence, minimum difference is 3.

# Input: arr[] = [1]
# Output: 1
# Explanation:
# Subset1 = {1}, sum of Subset1 = 1
# Subset2 = {}, sum of Subset2 = 0
# Hence, minimum difference is 1.

# Constraints:
# 1 ≤ arr.size()*|sum of array elements| ≤ 105
# 1 <= arr[i] <= 105

from functools import cache


class Solution:
    def minDifference(self, arr):
        total = sum(arr)

        @cache
        def rMinDifference(i, cur_sum):
            # Prune decision tree
            if cur_sum > total/2:
                return float("inf")

            if i == 0:
                return total - (2 * cur_sum)

            return min(
                rMinDifference(i-1, cur_sum + arr[i-1]),
                rMinDifference(i-1, cur_sum)
            )

        return rMinDifference(len(arr), 0)


if __name__ == "__main__":
    res = Solution()
    print(res.minDifference(arr=[1, 6, 11, 5]))
    print(res.minDifference(arr=[1, 4]))
    print(res.minDifference(arr=[1]))
