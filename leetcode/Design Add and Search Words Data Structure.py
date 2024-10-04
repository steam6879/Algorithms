class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.head = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.head

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.data = word

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.data

            char = word[i]
            if char in node.children:
                return dfs(node.children[char], i + 1)

            elif char == ".":
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True

            return False

        return dfs(self.head, 0)
