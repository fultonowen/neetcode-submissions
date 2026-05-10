class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        def backtrack(i: int, c_sum: int):
            nonlocal ans, nums, target, curr
            if c_sum > target: return
            if c_sum == target:
                ans.append(curr.copy())
                return
            
            for idx in range(i, len(nums)):
                curr.append(nums[idx])
                backtrack(idx, nums[idx] + c_sum)
                curr.pop()
        backtrack(0, 0)
        return ans