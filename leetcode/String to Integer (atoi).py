class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        s = s.replace(' ', '')

        for char in s:
            if char in {'-', '+'}:
                if not ans:
                    ans += char

            elif char.isalpha or char == '.':
                break

            else:
                ans += char

        return int(ans)


if __name__ == "__main__":
    print(Solution.myAtoi(Solution, s='45'))
