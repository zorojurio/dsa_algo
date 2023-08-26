class TrieNode:
    def __init__(self) -> None:
        self.children: dict = {}
        self.end_of_string = False

    def __repr__(self):
        return f"{self.children}"


class Trie:
    def __init__(self) -> None:
        self.root_node = TrieNode()

    def __repr__(self):
        return f"{self.root_node.children}"

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


def delete_string(root_node, word: str, index: int) -> bool:
    ch: str = word[index]
    current_node: TrieNode = root_node.children.get(ch)

    if len(current_node.children) > 1:
        # trie has some other prefixes that is why it has more than one child
        delete_string(current_node, word, index + 1)
        return False
    if index == len(word) - 1:
        # logic in the last Node
        if len(current_node.children) >= 1:
            # this node is a prefix of another node
            current_node.end_of_string = False
            return False
        else:
            # this is the last char, hence deleting
            root_node.children.pop(ch)
            return True
    if current_node.end_of_string:
        delete_string(current_node, word, index + 1)
        return False

    can_this_node_be_deleted = delete_string(current_node, word, index + 1)
    if can_this_node_be_deleted:
        root_node.children.pop(ch)
        return True
    else:
        return False


def deleteString(root, word, index=0):
    if index == len(word):
        return
    ch = word[index]
    curnode = root.children.get(ch)
    if not curnode:
        return print("String doesn't exist.")
    deleteString(curnode, word, index + 1)
    if index == len(word) - 1:
        # handling last Node
        if curnode.children:
            curnode.end_of_string = False
            return
        else:
            root.children.pop(ch)
            return
    if curnode.children:
        return
    elif curnode.end_of_string == True:
        return
    else:
        root.children.pop(ch)


if __name__ == '__main__':
    new_trie = Trie()
    print('\nCase 1')
    new_trie.insert_string('API')
    new_trie.insert_string('APPLE')
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APPLE'))
    print('Deleting')
    deleteString(new_trie.root_node, 'API', 0)
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APPLE'))

    print('\n Case 2')
    new_trie.insert_string('API')
    new_trie.insert_string('APIS')
    new_trie.insert_string('APPLE')
    deleteString(new_trie.root_node, 'API', 0)
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APIS'))
    print(new_trie.search_string('APPLE'))

    print('\nCase 3 Deleting APIS')
    new_trie.insert_string('API')
    new_trie.insert_string('APIS')
    new_trie.insert_string('APPLE')
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APIS'))
    print(new_trie.search_string('APPLE'))
    deleteString(new_trie.root_node, 'APIS', 0)
    print('Deleting APIS')
    print(new_trie.search_string('API'))
    print(new_trie.search_string('APIS'))
    print(new_trie.search_string('APPLE'))
    #
    print('\nCase 3')
    new_trie.insert_string('API')
    new_trie.insert_string('APIS')
    new_trie.insert_string('APPLE')
    new_trie.insert_string('A')
    print(new_trie.search_string('A'))
    deleteString(new_trie.root_node, 'A', 0)
    print(new_trie.search_string('A'))
    print(new_trie.search_string('API'))

    print('\nCase 4')
    new_trie.insert_string('API')
    new_trie.insert_string('APIS')
    new_trie.insert_string('APPLE')
    print(new_trie.search_string('APBSJKBSZP'))
    deleteString(new_trie.root_node, 'APPLESZP')
    print(new_trie.search_string('AP'))
