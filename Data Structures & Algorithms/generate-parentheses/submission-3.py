class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, left, right):
            nonlocal ans, n
            if left + right == 2 * n:
                ans.append(curr)
                return
            
            if left < n:
                backtrack(curr + "(", left + 1, right)
            
            if right < left:
                backtrack(curr + ")", left, right + 1)
        backtrack("", 0, 0)
        return ans
