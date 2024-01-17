class Solution:
    def isHappy(self, n: int) -> bool:
        m = set()
        val, calc = n ,0

        while val != 1:
            calc = 0
            for i in list(map(int, str(val))):
                calc += i * i
            
            if calc in m:
                return False
            
            m.add(int(calc))
            val = calc

        else:
            return True