
class TrieNode:
    def __init__(self) -> None:
        self.children: dict = {}
        self.end_of_string = False


class Trie:
    def __init__(self) -> None:
        self.root_node = TrieNode()

    def insert_string(self, word: str) -> None:
        current = self.root_node
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print('Added to Trie')


if __name__ == '__main__':
    new_trie = Trie()
    new_trie.insert_string('APP')
    new_trie.insert_string('APL')
    new_trie.insert_string('API')
