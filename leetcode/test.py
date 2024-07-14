# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        pl, pr = 1, n

        while pl <= pr:
            pc = (pl + pr) // 2

            if isBadVersion(pc):
                pr = pc - 1
            else:
                pl = pc + 1

        return pl


class Solution2:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        pl = 1
        pr = n

        while pl <= pr:
            pc = (pl + pr) // 2

            if isBadVersion(pc):
                if pc == 1:
                    return 1

                if not isBadVersion(pc - 1):
                    return pc
                else:
                    pr = pc - 1

            else:
                if isBadVersion(pc + 1):
                    return pc + 1
                else:
                    pl = pc + 1
            
        return -1