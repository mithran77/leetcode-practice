# 846. Hand of Straights

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
# and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

# Constraints:
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length


# Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from typing import List
from collections import deque, Counter

# Sorting (BF)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Early return for size mismatch
        if len(hand) % groupSize != 0:
            return False

        # Create a char count
        count = Counter(hand)

        hand.sort()
        for num in hand:
            if count[num] > 0:
                for i in range(num, num + groupSize):
                    if count[i] < 1:
                        return False
                    count[i] -= 1

        return True

# Time & Space Complexity
# Time complexity: O(nlogn)
# Space complexity: O(n)

# # Hashmap greedy
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         pass


if __name__ == '__main__':
    res = Solution()
    print(res.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
    print(res.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))


