class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for r in range(2, len(nums), 3):
            if nums[r] - nums[r-2] > k:
                return []
            else:
                ans.append(nums[r-2:r+1])
        return ans

