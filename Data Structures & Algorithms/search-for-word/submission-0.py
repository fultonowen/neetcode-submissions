class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, i) -> bool:
            nonlocal m, n, board, word
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or word[i] != board[r][c] or board[r][c] == '#':
                return False
            
            board[r][c] = '#'
            res_left = dfs(r, c -1, i+1)
            res_right = dfs(r, c + 1, i+1)
            res_up = dfs(r -1, c, i+1)
            res_down = dfs(r+1, c, i+1)
            board[r][c] = word[i]
            return res_left or res_right or res_up or res_down
        
        for i in range(0, m):
            for j in range(0, n):
                if word[0] == board[i][j] and dfs(i, j, 0):
                    return True
        return False