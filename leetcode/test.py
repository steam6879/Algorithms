from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        visited = [False] * len(accounts)
        email_to_accounts = defaultdict(list)
        ans = []

        # Build email-to-accounts mapping
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_to_accounts[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in email_to_accounts[email]:
                    if not visited[neighbor]:
                        dfs(neighbor, emails)

        # Process each account
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))

        return ans
