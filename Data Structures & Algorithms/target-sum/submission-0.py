class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        def backtrack(i: int, curr: int):
            nonlocal nums, ans
            if curr == 0 and i == len(nums):
                ans += 1
            if i >= len(nums):
                return
            
            backtrack(i+1, curr + nums[i])
            backtrack(i+1, curr - nums[i])
        
        backtrack(0, target)
        return ans