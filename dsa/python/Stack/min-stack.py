# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks. At most 3 * 104 calls will be made to push, pop, top, and getMin.

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.min_stack:
#             new_min = min(self.getMin(), val)
#             self.min_stack.append(new_min)
#         else:
#             self.min_stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]


class MinStack:

    def __init__(self, head=None):
        self.head = head

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(self.head.min, val), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


class Node:
    def __init__(self, val: int, min: int, next):
        self.val = val
        self.min = min
        self.next = next


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    # res = Solution()
    # minStack = MinStack()
    # print(minStack.push(-2))
    # print(minStack.push(0))
    # print(minStack.push(-3))
    # print(minStack.getMin()) # return -3
    # print(minStack.pop())
    # print(minStack.top())    # return 0
    # print(minStack.getMin()) # return -2

    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-1))
    print(minStack.getMin())  # return -2
    print(minStack.top())     # return -1
    print(minStack.pop())
    print(minStack.getMin())  # return -2
