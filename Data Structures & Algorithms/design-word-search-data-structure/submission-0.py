class TrieNode:
    def __init__(self, is_end: bool=False):
        self.is_end = is_end
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if not letter in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_end = True

    def search(self, word: str) -> bool:
        word_len = len(word)
        bfs_q = collections.deque()
        curr = self.root
        bfs_q.append((curr, 0))
        while bfs_q:
            qs = len(bfs_q)
            for _ in range(qs):
                node, level = bfs_q.popleft()
                if level == len(word) and node.is_end:
                    return True
                elif level >= len(word):
                    return False    
                if word[level] == '.':
                    for _, v in node.children.items():
                        bfs_q.append((v, level+1))
                elif word[level] in node.children:
                    bfs_q.append((node.children[word[level]], level + 1))
        return False

