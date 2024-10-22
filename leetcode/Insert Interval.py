from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:
            # 현재 interval이 newInterval보다 앞에 있는 경우
            if interval[1] < newInterval[0]:
                ans.append(interval)
            # 현재 interval이 newInterval보다 뒤에 있는 경우
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)

                return ans + intervals[intervals.index(interval):]
            # 현재 interval이 newInterval과 겹치는 경우
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        ans.append(newInterval)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
