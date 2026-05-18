class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1: return []
        ans, curr = [], ""
        digimap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i: int, curr: str):
            nonlocal ans, digimap, digits
            if len(curr) > len(digits): return
            if len(curr) == len(digits):
                ans.append(str(curr))
                return
            
            for ch in digimap[digits[i]]:
                backtrack(i+1, curr + ch)
        
        backtrack(0, curr)
        return ans