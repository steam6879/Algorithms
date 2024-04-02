class Solution:
    def reverseVowels(self, s: str) -> str:
        m = {'a', 'e', 'i', 'o', 'u'}
        vowels = []
        s = list(s)

        for char in s:
            if char.lower() in m:
                vowels.append(char)

        for i in range(len(s)):
            if s[i].lower() in m:
                s[i] = vowels.pop()

        return ''.join(s)
    

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
                
            else:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        
        return ''.join(s)
            
                      
    
if __name__ == "__main__":
    print(Solution.reverseVowels(Solution, s='aA'))