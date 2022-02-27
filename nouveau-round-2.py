# # Write a function to find if B is a sub-array of A. For B to be called a sub-array of A,
# # the elements of B shall occur in A in the same order and in consecutive indices.
# #
# # For example:
# # A = {3,2,7,1,4,6} and B = {7,1,4}. Here, B is a sub-array of A ==> TRUE
# # A = {3,2,7,1,4,6} and B = {7,4,1}. Here, B is not a sub array of A ==> FALSE
# # A = {7,3,2,4,6,1} and B = {7,4,1}. Here also, B is not a sub array of A ==> FALSE

# from typing import List


# class Solution:
#     def findSubArray(self, a, b):

#         # Handle base case
#         if b == a:
#             return True

#         # lpos = rpos = 0

#         for i, c in enumerate(a):
#             if c == b[0]:
#                 lpos = i
#                 try:
#                     for j, d in enumerate(b):
#                         if d != a[lpos]:
#                             break
#                         else:
#                             lpos += 1
#                 except IndexError:
#                     return False

#                 if j == len(b) - 1:
#                     return True

#         return False

# if __name__ == '__main__':
#     ans = Solution()
#     print(ans.findSubArray([3,2,7,1,4,6], [7,1,4]))
#     print(ans.findSubArray([3,2,7,1,4,6], [7,4,1]))
#     print(ans.findSubArray([7,3,2,4,6,1], [7,4,1]))


# Write a function to find if B is a sub-array of A. For B to be called a sub-array of A,
# the elements of B shall occur in A in consecutive indices (but they need NOT be in the same order).

# A = {3,2,7,1,4,6} and B = {7,1,4}. Here, B is a sub-array of A ==> TRUE
# A = {3,2,7,1,4,6} and B = {4,7,1}. Here also, B is a sub array of A ==> TRUE
# A = {7,3,2,4,6,1} and B = {7,4,1}. Here, B is not a sub array of A ==> FALSE
import copy


class Solution:
    def findSubArray(self, a, b):

        char_count = {}
        # Find char count of substring
        for c in b:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        # main
        for i, c in enumerate(a):
            if c in char_count:
                lpos = i
                test_count = copy.deepcopy(char_count) # Deep copy
                try:
                    for _ in range(len(b)):
                        if a[lpos] in test_count:
                            test_count[c] -= 1
                            lpos += 1
                        else:
                            return False
                except IndexError:
                    return False

                flag = True
                for v in test_count.values():
                    if v != 0:
                        flag = False
                return flag

        return False

if __name__ == '__main__':
    ans = Solution()
    print(ans.findSubArray([3,2,7,1,4,6], [7,1,4]))
    print(ans.findSubArray([3,2,7,1,4,6], [4,7,1]))
    print(ans.findSubArray([7,3,2,4,6,1], [7,4,1]))

