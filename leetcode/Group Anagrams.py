from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)

        for s in strs:
            # Sort the characters of the string to create a key
            sortedKey = tuple(sorted(s))
            # Add the string to the corresponding list in the dictionary
            groupedAnagrams[sortedKey].append(s)

        # Return the values of the dictionary as a list of lists
        return list(groupedAnagrams.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sCounters = [Counter(sCounter) for sCounter in strs]
        strs = set(strs)
        ans = []

        for sCounter in sCounters:
            bundle = []
            for str in strs:
                if Counter(str) == sCounter:
                    bundle.append(str)
                    # strs.remove(str)

            ans.append(bundle)

        ans = [list(sublist) for sublist in set(tuple(sorted(sub)) for sub in ans)]

        return ans


if __name__ == "__main__":
    print(Solution.groupAnagrams(Solution, strs=["eat", "tea", "tan", "ate", "nat", "bat"]))