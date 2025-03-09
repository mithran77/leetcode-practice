# 295. Find Median from Data Stream

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
# and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Constraints:
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.

# Follow up:
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


from typing import List
import heapq
from collections import defaultdict, deque
# preddy
# max heap

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Insert
        if self.max_heap and num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance
        if len(self.min_heap) > (len(self.max_heap) + 1):
            val = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > (len(self.min_heap) + 1):
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            v1 = self.min_heap[0]
            v2 = -self.max_heap[0]
            return (v1 + v2) / 2

# Time complexity: O(m∗logn) for addNum(), O(m) for findMedian().
# Space complexity: O(n)

# class MedianFinder:

#     def __init__(self):
#         self.data = SortedList()

#     def addNum(self, num: int) -> None:
#         self.data.add(num)

#     def findMedian(self) -> float:
#         length = len(self.data)
#         if len(self.data) % 2 == 0:
#             return (self.data[length // 2 - 1] + self.data[length // 2]) / 2
#         else:
#             return self.data[length // 2]

# Time complexity: O(m∗logn) for addNum(), O(log n) for findMedian().
# Space complexity: O(n)
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.__getitem__


if __name__ == '__main__':
    # ans = Solution()
    pass
