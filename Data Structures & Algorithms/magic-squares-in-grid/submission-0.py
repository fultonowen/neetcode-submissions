class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3: return 0
        squares = 0
        for s_r in range(0, m - 2):
            for s_c in range(0, n - 2):
                a = [grid[s_r+i][s_c + j] for i in range(3) for j in range(3)]
                if sorted(a) != list(range(1, 10)):
                    continue
                
                lines = [ sum(a[3*i:3*i+3]) for i in range(3)] + [sum(a[i::3]) for i in range(3)] + [ a[0] + a[4] + a[8], a[2] + a[4] + a[6]]
                if all(v == 15 for v in lines):
                    squares += 1
                

        return squares