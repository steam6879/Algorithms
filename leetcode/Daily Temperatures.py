from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []

        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)
            
        return result
    
if __name__ == "__main__":
    print(Solution.dailyTemperatures(Solution, T=[73,74,75,71,69,72,76,73]))