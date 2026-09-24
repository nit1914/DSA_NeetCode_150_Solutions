class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if node.children[index] is None:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(index, node):

            # All characters processed
            if index == len(word):
                return node.isEnd

            ch = word[index]

            # Normal character
            if ch != '.':
                position = ord(ch) - ord('a')
                child = node.children[position]

                if child is None:
                    return False

                return dfs(index + 1, child)

            # '.' can represent any character
            for child in node.children:
                if child is not None:
                    if dfs(index + 1, child):
                        return True

            return False

        return dfs(0, self.root)