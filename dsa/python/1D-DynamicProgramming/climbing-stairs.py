# 70. Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45

# class Solution:

#     def climbStairs(self, n: int) -> int:
#         if n <= 0:
#             return 0

#         fib_list = [1, 2]
#         needed_steps = n - len(fib_list)

#         if needed_steps:
#             for i in range(0, needed_steps):
#                 fib_list.append(fib_list[-2] + fib_list[-1])

#         return fib_list[n-1]

# # Bottom up DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f, s = 1, 1

#         for _ in range(n - 1): # [..., f, s, ...]
#             tmp = f
#             f = f + s
#             s = tmp

#         return f

from functools import cache

# Recursive
class Solution:
    # @cache
    # def climbStairs(self, n: int) -> int:
    #     if n < 2:
    #         return 1
    #     return self.climbStairs(n -1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        cache = {}

        def fib(n):
            if n == 0 or n == 1:
                cache[n] = 1
            if n not in cache:
                cache[n] = fib(n -1) + fib(n - 2)
            return cache[n]

        return fib(n)

# 0 1 2
# 0 1 2 3
# 0 1 2 3 5
# 0 1 2 3 5 8
# 0 1 2 3 5 8 13


if __name__ == '__main__':
    res = Solution()
    print(res.climbStairs(n = 2))
    print(res.climbStairs(n = 3))
    print(res.climbStairs(n = 5))


