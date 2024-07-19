from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row, col = len(mat), len(mat[0])
        que = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    que.append((i, j))

        visited = set()
        visited.update(que)
        count = 0

        while que:
            # take out the 1st element coordinate in the queue
            for _ in range(len(que)):
                x, y = que.popleft()
                # find the neighbor
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < row and 0 <= yy < col \
                        and (xx, yy) not in visited:
                        que.append((xx, yy))
                        visited.add((xx, yy))
                # update the cooresponding position value for (x, y)
                # here we split into 2 case
                if mat[x][y] == 0:
                    mat[x][y] = 0
                else:
                    mat[x][y] = mat[x][y] + count - 1

            count += 1

        return mat
