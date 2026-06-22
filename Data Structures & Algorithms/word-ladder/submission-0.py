class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                cand = word[:i] + '*' + word[i+1:]
                graph[cand].append(word)
        
        transformationLevel = 0
        seen = set([beginWord])
        bfs_q = collections.deque([beginWord])

        while bfs_q:
            qs = len(bfs_q)
            for _ in range(qs):
                curr = bfs_q.popleft()
                if curr == endWord:
                    return transformationLevel + 1
                for i in range(len(curr)):
                    candidate = curr[:i] + '*' + curr[i+1:]
                    for neighbor in graph[candidate]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            bfs_q.append(neighbor)
            transformationLevel +=1
        
        return 0