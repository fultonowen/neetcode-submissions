class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l: int, r: int) -> int:
            nonlocal heights
            return (r - l) * min(heights[r], heights[l])

        n = len(heights)
        max_area = 0
        l, r = 0, n-1

        while l < r:
            max_area = max(max_area, area(l, r))
            if heights[r] < heights[l]:
                r -=1
            else:
                l += 1
        return max_area

