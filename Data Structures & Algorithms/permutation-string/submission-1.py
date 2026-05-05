class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_values = [0] * 26
        for ch in s1:
            s1_values[ord(ch) - ord('a')] += 1
        
        left = 0
        for right in range(0, len(s2)):
            s1_values[ord(s2[right]) - ord('a')] -= 1
            while right - left + 1 > len(s1):
                s1_values[ord(s2[left]) - ord('a')] += 1
                left += 1
            if all([x == 0 for x in s1_values]):
                return True
        
        return False