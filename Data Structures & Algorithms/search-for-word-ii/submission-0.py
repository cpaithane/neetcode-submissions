class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

    def add_word(self, word: str) -> None:
        root = self

        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]

        root.ends = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # First add every word in the trie.
        root = TrieNode()
        for word in words:
            root.add_word(word)

        rows = len(board)
        cols = len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, root, word):
            # Base conditions
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] not in root.children):
                return

            # Visit r, c
            visited.add((r, c))
            # Append the word and if word is found in Trie, add to the res.
            word += board[r][c]
            # Then move to the next node
            root = root.children[board[r][c]]
            if root.ends == True:
                res.add(word)
            
            dfs(r+1, c, root, word)
            dfs(r-1, c, root, word)
            dfs(r, c+1, root, word)
            dfs(r, c-1, root, word)

            # Removed from visited.
            visited.remove((r, c))

        # Go through board and check if board[r][c] is present in Trie
        for r in range(0, rows):
            for c in range(0, cols):
                dfs(r, c, root, "")

        return list(res)