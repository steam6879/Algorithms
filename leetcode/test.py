class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(pairs[bracket])

            elif not stack or bracket != stack.pop():
                return False
            
        return not stack
