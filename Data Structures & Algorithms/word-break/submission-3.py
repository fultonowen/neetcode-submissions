class TrieNode:
    def __init__(self, is_end: bool = False):
        self.children = {}
        self.is_end = is_end
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_end = True

        dp = [False] * len(s)
        for i in range(0, len(s)):
            if i == 0 or dp[i-1] == True:
                curr = root
                j = i
                while j < len(s):
                    if s[j] not in curr.children:
                        break
                    curr = curr.children[s[j]]
                    if curr.is_end: dp[j] = True
                    j+=1


        return dp[-1]