class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patternMap = defaultdict(list)
        L = len(wordList[0])
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                patternMap[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, lvl = q.popleft()
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighborn in patternMap[pattern]:
                    if neighborn == endWord:
                        return lvl + 1
                    if neighborn not in visited:
                        visited.add(neighborn)
                        q.append((neighborn, lvl + 1))
        return 0


        

