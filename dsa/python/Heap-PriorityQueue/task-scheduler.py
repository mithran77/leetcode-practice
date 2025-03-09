# 621. Task Scheduler

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
# Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order,
# but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval,
# neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

# Constraints:
# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

from typing import List
from heapq import heapify, heappop, heappush
from collections import defaultdict, deque
# preddy
# max heap

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_count = defaultdict(int)
        for t in tasks:
            t_count[t] += 1

        free_q = [-1 * count for count in t_count.values()] # <count>
        heapify(free_q)

        idling_q = deque() # <count, idle_untill>
        time = 0

        while idling_q or free_q: # Scheduler/worker
            time += 1

            if free_q: # consume & move remaining to idling_q
                cnt = 1 + heappop(free_q)
                if cnt:
                    idling_q.append([cnt, time + n])

            if idling_q and idling_q[0][1] == time: # Once idle time is over, add back to free_q
                cnt, _ = idling_q.popleft()
                heappush(free_q, cnt)

        return time


if __name__ == '__main__':
    ans = Solution()
    print(ans.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
    print(ans.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
    print(ans.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))
    print(ans.leastInterval(tasks = ["B","C","D","A","A","A","A","G"], n = 1))
