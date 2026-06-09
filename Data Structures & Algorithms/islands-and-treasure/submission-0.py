class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        def search(i: int, j: int):
            nonlocal grid, m, n
            bfs_q = collections.deque([(i, j)])
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while bfs_q:
                c_r, c_c = bfs_q.popleft()

                for dr, dc in directions:
                    new_r = c_r + dr
                    new_c = c_c + dc
                    if not (0 <= new_r < m and 0 <= new_c < n): continue
                    if grid[new_r][new_c] == -1: continue

                    if grid[c_r][c_c] + 1 < grid[new_r][new_c]:
                        grid[new_r][new_c] = grid[c_r][c_c] +1 
                        bfs_q.append((new_r, new_c))



        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    search(r, c)
