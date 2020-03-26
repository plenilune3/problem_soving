class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.word_count = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head

        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)

            node = node.children[char]
            node.word_count += 1

        node.data = string

    def search(self, string):
        node = self.head
        depth = 0

        for char in string:
            if char in node.children:
                node = node.children[char]
                depth += 1
                if node.word_count == 1:
                    return depth
                elif node.data == string:
                    return depth
            else:
                return False


def solution(words):
    answer = 0
    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)

    return answer
