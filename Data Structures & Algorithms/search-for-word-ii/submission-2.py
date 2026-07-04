class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        path = set()    # (r, c)
        res = []
        trie = Trie()
        # checks if word from words is possible to form from current position(r, c)
        def dfs(r, c, node):
            letter = board[r][c]
            if letter not in node.children:
                return
            
            path.add((r, c))
            node = node.children[letter]

            if node.word:
                res.append(node.word)
                node.word = None
            
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in path:
                    dfs(nr, nc, node)

            path.remove((r, c))

        for word in words:
            trie.insert(word)
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return res