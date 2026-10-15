class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        values = sorted(set(nums))
        left = 0
        best = 0
        for r, x in enumerate(values):
            while x- values[left] >=n: left +=1
            best = max(best, r - left + 1)
        return n - best
