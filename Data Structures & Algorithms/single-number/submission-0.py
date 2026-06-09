class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v = 0
        for num in nums:
            v = v ^ num
        return v