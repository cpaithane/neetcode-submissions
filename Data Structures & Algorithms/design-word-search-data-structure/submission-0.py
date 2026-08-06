class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root

        for ch in word:            
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]

        root.ends = True

    def search(self, word: str) -> bool:
        root = self.root

        def searchCore(root, word, idx):

            for i in range(idx, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in root.children.values():
                        if searchCore(child, word, i + 1):
                            return True
                    return False
                else:
                    if ch not in root.children:
                        return False
                    root = root.children[ch]

            return root.ends

        return searchCore(root, word, 0)