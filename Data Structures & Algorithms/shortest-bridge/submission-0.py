class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        def bfs(i, j):
            nonlocal n, seen, grid
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            bfs_q = collections.deque([(i, j)])
            seen.add((i, j))
            while bfs_q:
                qs = len(bfs_q)
                for _ in range(qs):
                    r, c = bfs_q.popleft()
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if not (0 <= new_r < n and 0 <= new_c < n) or grid[new_r][new_c] == 0:
                            continue
                        if not (new_r, new_c) in seen:
                            seen.add((new_r, new_c))
                            bfs_q.append((new_r, new_c))
            
        for i in range(n):
            for j in range(n):
                if len(seen) > 0: break
                if grid[i][j] == 1:
                    bfs(i, j)
                    break
        print(seen)
        def bfs_cost():
            nonlocal seen, grid, n
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            bfs_q = collections.deque([item for item in seen])
            level = 0
            while bfs_q:
                qs = len(bfs_q)
                for _ in range(qs):
                    r, c = bfs_q.popleft()
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if not (0 <= new_r < n and 0 <= new_c < n):
                            continue
                        if grid[new_r][new_c] == 0:
                            grid[new_r][new_c] = 1
                            seen.add((new_r, new_c))
                            bfs_q.append((new_r, new_c))
                        if grid[new_r][new_c] == 1 and (new_r, new_c) not in seen:
                            return level
                        
                level +=1
            return -1

        return bfs_cost()
