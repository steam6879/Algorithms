class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        m = {}
        
        if len(pattern) != len(sList):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in m:
                if sList[i] not in m.values():
                    m[pattern[i]] = sList[i]
                else:
                    return False
            
            else:
                if m[pattern[i]] != sList[i]:
                    return False
            
        return True
    
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        m = {}
        
        if len(pattern) != len(sList):  
            return False
        if len(set(pattern)) != len(set(sList)):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]] = sList[i]
            
            elif m[pattern[i]] != sList[i]:
                return False
            
        return True
    
if __name__ == "__main__":
    print(Solution.wordPattern(Solution, pattern="abba", s="dog dog dog dog"))