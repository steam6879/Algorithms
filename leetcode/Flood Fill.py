from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(i, j):
            image[i][j] = color
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)

        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color:
            dfs(sr, sc)

        return image


class Solution2:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color:
            que = deque([(sr, sc)])

            while que:
                (i, j) = que.popleft()
                image[i][j] = color

                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        que.append((x, y))

        return image
