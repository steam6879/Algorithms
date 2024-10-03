def wordBreak(s, wordDict):
    # Create a set for faster lookup
    word_set = set(wordDict)
    
    # Initialize a boolean array to track if a substring can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True  # An empty string can always be segmented
 
    for i in range(1, len(s) + 1):
        for j in range(i):
            print("i= ", i)
            print("j= ", j)
            print(s[j:i])
            if dp[j] and s[j:i] in word_set:
                
                dp[i] = True
                print('true dp= ', dp)
                break
            print("dp =", dp)
            print("-----------------------")
    return dp[len(s)]
 
# Test cases
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(wordBreak(s1, wordDict1))  # Output: True