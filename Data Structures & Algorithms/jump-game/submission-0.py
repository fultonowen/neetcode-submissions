class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(0, n):
            if dp[i]:
                print(f"idx: {i} nums: {nums[i]}")
                for jumps in range(i, min(n, i + nums[i]+1)):
                    dp[jumps] = True
        print(dp)
        return dp[-1]