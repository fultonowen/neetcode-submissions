class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def search(i: int, j: int) -> int:
            nonlocal grid, m, n

            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + search(i+1, j) + search(i-1, j) + search(i, j+1) + search(i, j-1)
        
        area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = max(area, search(r, c))
        return area
