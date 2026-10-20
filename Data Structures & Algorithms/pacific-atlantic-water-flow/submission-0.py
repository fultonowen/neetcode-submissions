class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = []
        # Atlantic = in m-1 row or n-1 col
        # Pacific = in 0 row or 0 col
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def bfs(entries: list, ocean):
            nonlocal m, n, heights, directions
            bfs_q = collections.deque(entries)

            while bfs_q:
                r, c = bfs_q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    n_r, n_c = r + dr, c + dc

                    if not (0 <= n_r < m and 0 <= n_c < n):
                        continue
                    if ocean[n_r][n_c]:
                        continue
                    if heights[r][c] > heights[n_r][n_c]:
                        continue
                    bfs_q.append((n_r, n_c))
        
        # bfs from pacific
        pacific = []
        atlantic = []
        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m-1, i))
        
        for j in range(m-1):
            pacific.append((m-j-1, 0))
            atlantic.append((j, n-1))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    ans.append([i, j])
        
        
        return ans
