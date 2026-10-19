class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
            
                if cell in rows[i] or cell in cols[j] or cell in boxes[(i//3, j//3)]:
                    return False
                
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[(i//3, j//3)].add(cell)
        return True