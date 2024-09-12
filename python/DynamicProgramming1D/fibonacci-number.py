# 509. Fibonacci Number
# Easy
# Topics
# Companies
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
# Constraints:
#
# 0 <= n <= 30
#

# # Recursive no optimizations
# class Solution:
#     def fib(self, n: int) -> int:
#         # BCs
#         if n < 2:
#             return n

#         # RC
#         return self.fib(n - 1) + self.fib(n -2)

# # Recursive with Memoization
# class Solution:
#     def fib(self, n: int) -> int:

#         cache = { 0 : 0, 1 : 1 }

#         def fastFib(n, cache):
#             if n in cache:
#                 return cache[n]

#             return fastFib(n - 1, cache) + fastFib(n - 2, cache)

#         return fastFib(n, cache)

# Memoization without auxilary stack
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev2, prev = 0, 1

        for _ in range(2, n + 1):
            cur = prev + prev2
            prev2, prev = prev, cur

        return prev

if __name__ == '__main__':
    res = Solution()
    print(res.fib(n = 0))
    print(res.fib(n = 2))
    print(res.fib(n = 3))
    print(res.fib(n = 4))

