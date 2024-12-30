# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


from typing import List

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         def dfs(cur, size):
#             # BC
#             if size == (n * 2):
#                 if self.isValidString(cur):
#                     res.append(cur)
#                 return
#             if self.openMoreThanClose(cur):
#                 # Take open
#                 dfs(cur + '(', size + 1)
#                 # Take close
#                 dfs(cur + ')', size + 1)

#         dfs("", 0) 
#         return res

#     def openMoreThanClose(self, s: str) -> bool:
#         c_count = {}
#         for c in s: c_count[c] = 1 + c_count.get(c, 0)
#         if c_count.get('(', 0) >= c_count.get(')', 0):
#             return True
#         return False

#     def isValidString(self, str) -> bool:
#         stack = []
#         for c in str:
#             if c == '(':
#                 stack.append(c)
#             else:
#                 if not stack or stack.pop() != '(':
#                     return False

#         return len(stack) == 0

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def dfs(o_cnt, c_cnt):
            if o_cnt == n and c_cnt == n:
                ans.append("".join(stack))
                return

            if o_cnt < n:
                stack.append('(')
                dfs(o_cnt + 1, c_cnt)
                stack.pop()

            if c_cnt < o_cnt:
                stack.append(')')
                dfs(o_cnt, c_cnt + 1)
                stack.pop()

        dfs(0, 0)
        return ans

if __name__ == '__main__':
    res = Solution()
    print(res.generateParenthesis(n = 3))
    print(res.generateParenthesis(n = 1))


# RT
#
# dfs(0, 0); stack = []
# dfs(1, 0); stack = [(]
# dfs(2, 0); stack = [((]
# dfs(3, 0); stack = [(((]
# dfs(3, 1); stack = [((()]
# dfs(3, 2); stack = [((())]
# dfs(3, 3); stack = [((()))]; ans

# [((())]
# [((()]
# [(((]
# [((]

# dfs(2, 1); stack = [(()]
# dfs(3, 1); stack = [(()(]
# dfs(3, 2); stack = [(()()]
# dfs(3, 3); stack = [(()())]; ans

# [(()()]
# [(()(]
# [(()]

# dfs(2, 2); stack = [(())]
# dfs(3, 2); stack = [(())(]
# dfs(3, 3); stack = [(())()]; ans

# [(())(]
# [(())]
# [(()]
# [((]
# [(]

# dfs(1, 1); stack = [()]
# dfs(2, 1); stack = [()(]
# dfs(3, 1); stack = [()((]
# dfs(3, 2); stack = [()(()]
# dfs(3, 3); stack = [()(())]; ans

# [()(()]
# [()((]
# [()(]

# dfs(2, 2); stack = [()()]
# dfs(3, 2); stack = [()()(]
# dfs(3, 3); stack = [()()()]; ans

# [()()(]
# [()()]
# [()(]
# [()]
# [(]
# []

