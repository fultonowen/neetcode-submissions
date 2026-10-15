class TrieNode:
    def __init__(self, is_end: bool = False):
        self.children = {}
        self.is_end = is_end
    
    def add_to_node(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add_to_node(word)
        
        directions = [(-1, 0), (0, 1), (1,0), (0, -1)]
        ans = set()
        seen = set()
        def backtrack(r: int, c: int, so_far: str, node: TrieNode):
            nonlocal m, n, board, seen, directions
            if so_far not in ans and node.is_end:
                ans.add(so_far[:])
            
            if len(so_far) > 10:
                return
            
            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                if not (0 <= n_r < m and 0 <= n_c < n):
                    continue
                if (n_r, n_c) in seen or board[n_r][n_c] not in node.children:
                    continue
                seen.add((n_r, n_c))
                backtrack(n_r, n_c, so_far + board[n_r][n_c], node.children[board[n_r][n_c]])
                seen.remove((n_r, n_c))

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] not in root.children:
                    continue
                seen.add((i, j))
                backtrack(i, j, board[i][j], root.children[board[i][j]])
                seen.clear()
        
        return list(ans)
                


