from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keyboard = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        ans = []

        def dfs(index, path):
            if index == len(digits):
                return ans.append(path)

            for char in keyboard[digits[index]]:
                dfs(index + 1, path + char)

        dfs(0, "")
        return ans
