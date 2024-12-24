# from collections import deque

class Solution(object):
    def isValid(self, s):
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


class Solution2:     # 24.5.6. ~ my solution in grind 98
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[' : ']',
             '{' : '}',
             '(' : ')'}
        
        for bracket in s:
            if bracket in pairs:
                stack.append(pairs[bracket])

            elif not stack or bracket != stack.pop():
                return False
                
        return not stack
    
# class Solution:
#     def isValid(self, s: str) -> bool:
#         lst = s.list()
#         deq = deque()
#         for i in lst:
#             if deq[-1] in ['(', '[', '{']:
#                 if i in [')', ']', '}']:
#                     return True
                
#                 else:

                
#         return False








        # lst = list(s)

        # if len(lst) <= 1:
        #     return False
        
        # for i in range(len(lst)):
        #     if s[i:i + 2] not in ['()', '[]', '{}']:
        #         return False

        # return True

        
if __name__ == '__main__':
    sol = Solution()
    s = "(]"
    print(sol.isValid(s))