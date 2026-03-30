class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == INF:
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))

# add all 0's cells to a queue and then start bfs function