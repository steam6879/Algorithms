from typing import List
from collections import Counter

nums = [0, 0, 1, 0, 0, 0, 1, 1]
prefixSum = [0] * len(nums)
prefixSum[0] = -1 if nums[0] == 0 else 1

for i in range(1, len(nums)):
    if nums[i] == 0:
        prefixSum[i] = prefixSum[i - 1] - 1
    else:
        prefixSum[i] = prefixSum[i - 1] + 1

m = Counter(prefixSum)

maxKey = max(m, key = m.get)
i1 = prefixSum.index(maxKey)
i2 = len(prefixSum) - 1 - prefixSum[::-1].index(maxKey)

print(i1, i2)