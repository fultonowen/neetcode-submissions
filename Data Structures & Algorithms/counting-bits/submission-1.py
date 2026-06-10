class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        if n == 2: return [0, 1, 1]
        dp = [0] * (n +1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i>>1] + (i & 1)
        
        return dp