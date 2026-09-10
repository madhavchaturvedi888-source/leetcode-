class Solution:
    def uniquePathsIII(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        start_r = start_c = 0
        empty = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    empty += 1
                if grid[r][c] == 1:
                    start_r, start_c = r, c

        def dfs(r, c, visited):
            if grid[r][c] == 2:
                return 1 if visited == empty else 0

            total = 0
            grid[r][c] = -1

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] != -1):

                    total += dfs(nr, nc, visited + 1)

            grid[r][c] = 0
            return total

        return dfs(start_r, start_c, 1)