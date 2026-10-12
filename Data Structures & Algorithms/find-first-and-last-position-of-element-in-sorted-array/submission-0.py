class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(compare):
            nonlocal nums, target
            l, r = 0, len(nums)

            while l < r:
                mid = (l + r) // 2
                if compare(nums[mid], target):
                    l = mid + 1
                else:
                    r = mid
            return l
        
        lower = search(lambda x, y: x < target)
        if lower >= len(nums) or nums[lower] != target:
            return [-1, -1]
        upper = search (lambda x, y: x <= target) - 1
        return [lower, upper]