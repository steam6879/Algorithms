from collections import defaultdict, deque


indegree = defaultdict(int)
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
que = []
graph = defaultdict(list)
for a, b in prerequisites:
    graph[b].append(a)
    indegree[a] += 1

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

for node in graph:
    if indegree[node] == 0:
        que.append(node)

print(graph)
print(indegree)