from collections import defaultdict


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.length = defaultdict(int)


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string, length):
        node = self.head
        node.length[length] += 1

        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)

            node.children[char].length[length] += 1
            node = node.children[char]

        node.data = string

    def starts_with(self, prefix, length):
        node = self.head

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return node.length[length]


def solution(words, queries):
    answer = []
    trie_forward = Trie()
    trie_backward = Trie()

    for word in words:
        length_word = len(word)
        trie_forward.insert(word, length_word)
        trie_backward.insert(word[::-1], length_word)

    for query in queries:
        length_query = len(query)

        if query[0] != '?':
            prefix = query.replace('?', '')
            answer.append(trie_forward.starts_with(prefix, length_query))
        else:
            suffix = query.replace('?', '')[::-1]
            answer.append(trie_backward.starts_with(suffix, length_query))

    return answer
