# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.


# x = 2
# y = 10


# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.


# class Solution:
#     def hammingDistance(self, a, b):
#         a = str(bin(a))[2:]
#         b = str(bin(b))[2:]
#         c = 0

#         max_len = max(len(a), len(b))
#         req_a = max_len - len(a)
#         req_b = max_len - len(b)

#         for _ in range(req_a):
#             a = '0' + a
#         for _ in range(req_b):
#             b = '0' + b

#         for i in range(max_len):
#             if a[i] != b[i]:
#                 c += 1
        
#         return c


# if '__main__' == __name__:
#     ans = Solution()
#     print(ans.hammingDistance(1, 4))

