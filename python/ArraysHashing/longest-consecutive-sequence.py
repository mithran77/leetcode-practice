from typing import List
import collections

# class Solution:

#     def longestConsecutive(self, nums: List[int]) -> int:

#         snums = sorted(list(set(nums)))
#         if len(snums) == 1:
#             return 1

#         cnt, tmp_cnt = 0, 1

#         for i in range(len(snums)-1):
#             if snums[i] + 1 == snums[i+1]:
#                 tmp_cnt += 1
#             else:
#                 tmp_cnt = 1
#             cnt = max(cnt, tmp_cnt)

#         return cnt

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in snums:
                length = 0
                while (n + length) in snums:
                    length += 1
                
                longest = max(longest, length)

        return longest

if __name__ == '__main__':
    res = Solution()
    print(res.longestConsecutive([100,4,200,1,3,2]))
    print(res.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(res.longestConsecutive([1,2,0,1]))
    print(res.longestConsecutive([100,4,200,1,3,2]))
    print(res.longestConsecutive([0,0]))

