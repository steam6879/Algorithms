from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:    # case 1
                ans.append(intervals[i])

            elif intervals[i][0] > newInterval[1]:  # case 3
                ans.append(newInterval)

                return ans + intervals[i:]

            else:   # case 2
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        ans.append(newInterval)

        return ans


if __name__ == '__main__':
    print(Solution.insert(Solution, intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
