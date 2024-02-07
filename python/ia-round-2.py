

# import re


# TC = [
#     'rafi@gmail.com',
#     'rafi@impact.com',
#     'pqr.impact.com',
#     'lmn@impact.co',
#     'abc.com',
#     'pqrimapact.com',
#     'test@impact.com',
#     'rafi.ahmad123@impact.com',
#     'rafi*ahmad123@impact.com',
#     'rafi.ahmad123@impact.comabctest',
#     'test1@impact.com@gmail.com',
#     'test1@impact.com@impact.com'
# ]


# class Solution:
#     def validEmail(self, emails):
#         for email in emails:
#             regex = r'\b[A-Za-z0-9._%+-]+\@impact\.com$'
#             if(re.fullmatch(regex, email)):
#                 print(f'{email}')

# if __name__ == '__main__':
#     res = Solution()
#     res.validEmail(TC)


# SQL
class Parent(object):
   # Constructor
   def __init__(self, name):
       self.name = "test"


class Child(Parent):
   # Constructor
   def __init__(self, name, age):
       self.age = age
       # print name here
       Parent.__init__(self, name)
       print(self.name)

if __name__ == '__main__':
    res = Child('mithran', 35)
    print(res.name)
    # res.validEmail(TC)