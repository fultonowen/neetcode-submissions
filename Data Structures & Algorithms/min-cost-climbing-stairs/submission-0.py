class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        if n < 2: return cost[0]
        if n < 3: return min(cost[0], cost[1])

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[-1]