class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        seen = set()
        def backtrack():
            nonlocal nums, ans, curr, seen
            if len(curr) == len(nums):
                ans.append(list(curr))
                return
            
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtrack()
                    curr.pop()
                    seen.remove(num)
        
        backtrack()
        return ans