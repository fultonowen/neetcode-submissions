class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        end_idx = 0
        for i in range(end_idx, n):
            if nums[i]:
                nums[i], nums[end_idx] = nums[end_idx], nums[i]
                end_idx += 1
        