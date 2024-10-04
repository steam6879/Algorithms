class WordDictionary:
    def __init__(self):
        self.root = {"$": True}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {"$": False}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node["$"]
            ch = word[idx]
            if ch in node:
                return dfs(node[ch], idx + 1)
            if ch == ".":
                return any(dfs(node[k], idx + 1) for k in node if k != "$")

        return dfs(self.root, 0)
    


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end
            
            character = word[i]
            if character == '.':
                for character in node.children:
                    if dfs(i+1, node.children[character]):
                        return True
            elif character in node.children:
                return dfs(i+1, node.children[character])
        return dfs(0, self.root)
