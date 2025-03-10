# 2251. Number of Flowers in Full Bloom
# Hard
# Topics
# Companies
# Hint
# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from 
# starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith 
# person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

# Example 1:

# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
# Example 2:

# Input: flowers = [[1,10],[3,3]], people = [3,3,2]
# Output: [2,2,1]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.

# Constraints:

# 1 <= flowers.length <= 5 * 104
# flowers[i].length == 2
# 1 <= starti <= endi <= 109
# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= 109

from typing import List
import heapq

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [ (p, i) for i, p in enumerate(people) ] 
        start = [ f[0] for f in flowers ]
        end = [ f[1] for f in flowers ]
        heapq.heapify(start)
        heapq.heapify(end)
        res = [0] * len(people)
        count = 0

        for p, i in sorted(people):

            while start and start[0] <= p:
                count += 1
                heapq.heappop(start)

            while end and end[0] < p:
                count -= 1
                heapq.heappop(end)

            res[i] = count

        return res

if __name__ == '__main__':
    res = Solution()
    print(res.fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
    print(res.fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))

