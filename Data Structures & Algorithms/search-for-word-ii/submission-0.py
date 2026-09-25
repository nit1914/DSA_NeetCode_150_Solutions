
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        # Step 1: Build the Trie
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # Step 2: DFS + Backtracking
        def dfs(r, c, parent):
            char = board[r][c]

            # Stop if character is not a valid prefix
            if char not in parent.children:
                return

            node = parent.children[char]

            # Step 3: Check if a complete word is found
            if node.word is not None:
                result.append(node.word)
                node.word = None  # Avoid duplicates

            # Step 4: Mark current cell as visited
            board[r][c] = "#"

            # Step 5: Explore four directions
            for dr, dc in [(1, 0), (-1, 0),
                           (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):
                    dfs(nr, nc, node)

            # Step 6: Restore the cell
            board[r][c] = char

            # Step 7: Prune exhausted Trie branches
            if not node.children and node.word is None:
                del parent.children[char]

        # Step 8: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result