# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]


# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.


from typing import List
# from collections import deque, Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Compute highest indexes
        last_index = {}
        res = []
        for i, c in enumerate(s):
            last_index[c] = i

        # Use a running max to keep track 
        # of the maximum index we need to partition at
        size, max_index = 0, 0

        for i, c in enumerate(s):
            size += 1
            max_index = max(max_index, last_index[c])

            if i == max_index:
                res.append(size)
                size = 0

        return res


if __name__ == '__main__':
    res = Solution()
    print(res.partitionLabels(s = "ababcbacadefegdehijhklij"))
    print(res.partitionLabels(s = "eccbbbbdec"))

