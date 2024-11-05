# 875. Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


from typing import List
import math

# # Brute Force 1
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         piles.sort()
#         k = piles[len(piles) - 1]
#         # Start from max and keep deducting 1

#         for i in range(piles[len(piles) - 1], -1, -1):
#             tmp = piles.copy()
#             cnt = 0
#             for j in range(len(tmp)):
#                 cnt += math.ceil(piles[j] / i)
#             if cnt > h:
#                 break
#             k = min(k, i)

#         return k

# # Brute Force 2
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         speed = 1

#         while True:
#             total_time = 0
#             for pile in piles:
#                 total_time += math.ceil(pile / speed)

#             if total_time <= h:
#                 return speed

#             speed += 1

# Binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r

        while l <= r:
            m = l + ((r-l) // 2)

            total_time = 0
            for p in piles:
                total_time += math.ceil(p/m)
            if total_time <= h:
                speed = m
                r = m - 1
            else:
                l = m + 1

        return speed


if __name__ == '__main__':
    res = Solution()
    print(res.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(res.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(res.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
