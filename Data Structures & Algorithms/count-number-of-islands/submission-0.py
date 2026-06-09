class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def search(i: int, j: int):
            nonlocal grid, m, n
            
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            search(i+1, j)
            search(i-1, j)
            search(i, j+1)
            search(i, j-1)
        
        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    search(r, c)
                    islands +=1
        return islands
            