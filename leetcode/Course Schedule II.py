from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        que = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)

        ans = []
        while que:
            node = que.popleft()
            ans.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    que.append(neighbor)

        if len(ans) != numCourses:
            return []

        return ans


if __name__ == "__main__":
    print(Solution.findOrder(Solution, numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
