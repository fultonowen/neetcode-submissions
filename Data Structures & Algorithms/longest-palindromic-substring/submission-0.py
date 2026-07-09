class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximumLen = 0
        res_idx = 0
        def from_center(i: int, j: int):
            nonlocal s, maximumLen, res_idx

            while i >=0 and j < len(s) and s[i] == s[j]:
                if (j-i + 1) > maximumLen:
                    res_idx = i
                    maximumLen = (j-i+1)
                i-=1
                j+=1
            

        for i in range(0, len(s)):
            s1 = from_center(i, i)
            s2 = from_center(i, i+1)
        return s[res_idx:(res_idx + maximumLen)]
        

