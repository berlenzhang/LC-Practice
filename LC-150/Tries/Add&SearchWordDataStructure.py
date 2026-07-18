class TrieNode:
    def __init__(self):
        self.children = {}
        self.last_char = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.last_char = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, root):
            curr = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.last_char
        return dfs(0, self.root)