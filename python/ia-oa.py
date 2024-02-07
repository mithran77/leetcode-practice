# Please solve the below Problem statement and send the solution in a Github repo.

# ## Question

# In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
# You are not allowed to miss classes for four or more consecutive days. 
# Your graduation ceremony is on the last day of the academic year, which is the Nth day.

# Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
# Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't 
# actually divide or reduce the fraction to decimal
# Test cases:

# for 5 days: 14/29

# for 10 days: 372/773

import itertools


# Brute Force
class Solution:
    def checkAttendance(self, n):
        comb = list(itertools.product('AP', repeat=n))
        comb_str = [ ''.join(c) for c in comb ]

        # 1
        fail_comb = i = 0
        while i < len(comb_str):
            if comb_str[i].find('AAAA') >= 0:
                fail_comb += 1
                del(comb_str[i])
            else:
                i += 1

        one = len(comb_str)

        # 2
        two = 0
        for s in comb_str:
            if s[-1] == 'A':
                two += 1

        return str(two) + '/' + str(one)

# # Optimized
# class Solution:
#     def checkAttendance(self, n):
#         # Recursive fact
#         def fact(n):
#             if n == 0:
#                 return 1
#             else:
#                 n = n * fact(n-1)
#             return n

#         i = int(n/2)
#         p = w = 0

#         while i <= n:
#             w = w + int(fact(i+1) / (fact(n-i) * fact(2*i-n+1)))
#             if i < n:
#                 p = p + int(fact(i) / (fact(n-i-1) * fact(2*i-n+1)))
#             i = i + 1

#         return (str(p) + "/" + str(w))


if __name__ == '__main__':
    res = Solution()
    print(res.checkAttendance(5))
    print(res.checkAttendance(10))
