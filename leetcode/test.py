trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
n = 4
m = {}
for i in range(len(trust)):
    a, b = trust[i][0], trust[i][1]
    m[a] = m.get(a, []) + [b]
    # m[b] = m.get(b, []) + [a]
print(m)