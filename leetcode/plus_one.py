from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigits = ''

        for s in digits:
            strDigits += str(s)

        incrDigits = int(strDigits) + 1
        ans = list(map(int, str(incrDigits)))

        return ans