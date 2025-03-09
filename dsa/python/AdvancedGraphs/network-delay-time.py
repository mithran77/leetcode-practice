# 743. Network Delay Time

# You are given a network of n nodes, labeled from 1 to n. You are also given times,
# a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.


# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1


# Constraints:
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)


from typing import List
from collections import defaultdict, deque
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        adj = defaultdict(set)
        for v, n, w in times:
            adj[v].add((n, w))

        visited = set()
        min_heap = [(0, k)]
        max_time = 0

        while min_heap:
            dist, node = heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)

            max_time = max(max_time, dist)

            for nei, nei_dist in adj[node]:
                new_dist = dist + nei_dist
                heappush(min_heap, (new_dist, nei))

        return max_time if len(visited) == n else -1

if __name__ == '__main__':
    res = Solution()
    print(res.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(res.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
    print(res.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))


