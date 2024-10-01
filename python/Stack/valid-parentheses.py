# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         fifoStack = []
#         brackets = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }

#         for c in s:

#             # Push open brackets
#             if c in brackets.values():
#                 fifoStack.append(c)
#             # Pop close brackets
#             if c in brackets:
#                 # Base case
#                 if len(fifoStack) < 1:
#                     return False
#                 # Main case
#                 if fifoStack[-1] != brackets[c]:
#                     return False
#                 else: # Continue
#                     fifoStack.pop()

#         if fifoStack != []:
#             return False

#         return True


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         b_map = { '(': ')', '[': ']', '{': '}' }

#         for c in s:
#             need_close = b_map.get(c)
#             if need_close:
#                 stack.append(need_close)
#             elif not stack or c != stack.pop():
#                 return False

#         return stack == []

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in brackets: # Opening
                stack.append(c)
                continue
            elif not stack or stack[-1] != brackets[c]:
                return False
            stack.pop()

        return stack == []

if __name__ == '__main__':
    res = Solution()
    print(res.isValid("()"))
    print(res.isValid("()[]{}"))
    print(res.isValid("(]"))
    print(res.isValid("([])"))
