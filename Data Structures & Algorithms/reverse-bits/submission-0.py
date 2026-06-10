class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 0
        while i < 32:
            ans += (n >> i) & 1
            ans <<= 1
            i+=1 
        return ans // 2