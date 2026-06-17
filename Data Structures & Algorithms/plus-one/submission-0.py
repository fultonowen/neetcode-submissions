class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 < 10:
            digits[-1] +=1 
            return digits
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            v = carry + digits[i]
            digits[i] = v % 10
            carry = 1 if v > 9 else 0
        
        if carry == 1:
            digits = [1] + digits
        return digits
