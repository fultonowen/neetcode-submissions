class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        bfs_q = collections.deque([(sr, sc)])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        start_color = image[sr][sc]
        if start_color == color: return image
        image[sr][sc] = color
        while bfs_q:
            r, c = bfs_q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if not (0 <= row < m and 0 <= col < n):
                    continue
                
                if image[row][col] == start_color:
                    bfs_q.append((row, col))
                    image[row][col] = color
        
        return image