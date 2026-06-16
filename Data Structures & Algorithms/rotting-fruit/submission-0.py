class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs_q = collections.deque()
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    bfs_q.append((i, j))
        
        if not bfs_q and fresh_count > 0:
            return -1

        minutes = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while bfs_q:
            qs = len(bfs_q)
            if fresh_count == 0:
                return minutes

            for _ in range(qs):
                r, c = bfs_q.popleft()

                for dr, dc in directions:
                    n_r, n_c = r + dr, c + dc
                    if not (0 <= n_r < m and 0 <= n_c < n):
                        continue
                    if grid[n_r][n_c] == 1:
                        fresh_count -= 1
                        bfs_q.append((n_r, n_c))
                        grid[n_r][n_c] = 2
                    
            minutes += 1
        
        return minutes if fresh_count == 0 else -1


        
