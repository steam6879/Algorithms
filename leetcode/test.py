from collections import Counter
strs = ["eat","tea","tan","ate","nat","bat"]
sCounters = [Counter(sCounter) for sCounter in strs]
print(sCounters)