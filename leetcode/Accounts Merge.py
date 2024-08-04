from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        visited = [False] * len(accounts)  # A list to keep track of which accounts have been visited
        m = defaultdict(list)  # A dictionary that maps each email to a list of account indices containing that email
        ans = []  # This will store the final result, a list of merged accounts

        # Build the email-to-accounts mapping
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):  # Iterate through all emails in the current account
                email = account[j]
                m[email].append(i)  # Append the current account index to the list for this email

        # DFS function to explore all accounts connected via emails
        def dfs(i, emails):
            if visited[i]:  # If the current account has already been visited, do nothing
                return None  # Incorrect: should just `return` without `None`

            visited[i] = True  # Mark the current account as visited
            for j in range(1, len(accounts[i])):  # Iterate through all emails in the current account
                email = accounts[i][j]
                emails.add(email)  # Add the email to the set of emails for the current connected component

                for neighbor in m[email]:  # Explore all accounts linked via the current email
                    if not visited[neighbor]:  # Only visit accounts that haven't been visited
                        dfs(neighbor, emails)  # Recur to explore connected accounts

        # Process each account to find all connected accounts
        for i, account in enumerate(accounts):
            if visited[i]:  # Skip already visited accounts
                continue

            name = account[0]  # The name of the account, which is the first element in the account list
            emails = set()  # A set to store all unique emails for the current connected component
            dfs(i, emails)  # Start DFS from the current account to gather all connected emails
            ans.append([name] + sorted(emails))  # Append the result for the current connected component

        return ans  # Return the final list of merged accounts

if __name__ == "__main__":
    print(Solution.accountsMerge(Solution, accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))