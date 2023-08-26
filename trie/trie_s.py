
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

    def search_string(self, word: str) -> bool:
        current_node: TrieNode = self.root_node
        for i in word:
            node = current_node.children.get(i)
            if node is None:
                return False
            current_node = node
        if current_node.end_of_string:
            return True
        return False


if __name__ == '__main__':
    new_trie = Trie()
    new_trie.insert_string('APP')
    new_trie.insert_string('APL')
    new_trie.insert_string('API')
    new_trie.insert_string('APIS')
    print(new_trie.search_string('AP'))
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APIS'))
