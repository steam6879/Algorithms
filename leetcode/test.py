from collections import Counter
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sCounters = [Counter(sCounter) for sCounter in strs]
print(sCounters)
strs = set(strs)
print(strs)

ans1 = [['ate', 'tea', 'eat'], ['ate', 'tea', 'eat'], ['nat', 'tan'], ['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']]

# 중복 제거를 위해 set을 이용하여 각 서브리스트를 집합으로 변환한 후 다시 리스트로 변환
unique_sublists = [list(sublist) for sublist in set(tuple(sorted(sub)) for sub in ans1)]

ans2 = unique_sublists

print(ans2)
