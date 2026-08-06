class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Build the graph with all possible patterns of the word from wordList
        # Do BFS from beginWord to endWord.

        # endWord must be in wordList
        if endWord not in wordList:
            return 0

        # beginWord must in wordList
        wordList.append(beginWord)

        # Build the graph of pattern->list of words
        graph = {}
        for word in wordList:
            for i in range(0, len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors = graph.get(pattern, [])
                neighbors.append(word)
                graph[pattern] = neighbors

        # Start BFS from beginWord
        q = deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        steps = 1

        while q:
            # Go through layers
            for i in range(0, len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps

                # Build the pattern for neighbors
                for j in range(0, len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for n in graph[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            
            steps += 1

        return 0