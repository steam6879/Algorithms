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


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return 0  # Empty string case

        ans = 0
        sign = 1
        i = 0

        # Check for leading sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Process numerical characters
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Check for integer overflow
            if ans > (2**31 - 1) // 10 or (ans == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31

            ans = ans * 10 + digit
            i += 1

        return sign * ans


if __name__ == "__main__":
    print(Solution.myAtoi(Solution, s='45'))
