# 45. Jump Game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


from typing import List
from collections import deque


# BFS
class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = set()
        q = deque([0])
        depth = 0

        while q:
            size = len(q)
            for _ in range(size):
                start = q.popleft()
                if start == len(nums) - 1:
                    return depth
                end = start + nums[start] + 1
                for j in range(start + 1, end):
                    if j not in visited:
                        q.append(j)
                        visited.add(j)
            depth += 1
        
        return -1

if __name__ == '__main__':
    res = Solution()
    print(res.jump(nums = [2,3,1,1,4]))
    print(res.jump(nums = [2,3,0,1,4]))
    print(res.jump(nums = [2,1,1,1,1]))
