class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        curr = self.head

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.data = word

    def search(self, word: str) -> bool:
        curr = self.head

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        if curr.data:
            return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return True
