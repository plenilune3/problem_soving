from sys import setrecursionlimit

setrecursionlimit(1000000)


class Node:
    def __init__(self, number, data):
        self.number = number
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    preorder = []
    postorder = []

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, node, node_new):
        if node.data > node_new.data:
            if node.left is None:
                node.left = node_new
            else:
                self._insert(node.left, node_new)
        else:
            if node.right is None:
                node.right = node_new
            else:
                self._insert(node.right, node_new)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder(self.root)

    def _preorder(self, node):
        self.preorder.append(node.number)
        if node.left is not None:
            self._preorder(node.left)
        if node.right is not None:
            self._preorder(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder(self.root)

    def _postorder(self, node):
        if node.left is not None:
            self._postorder(node.left)
        if node.right is not None:
            self._postorder(node.right)
        self.postorder.append(node.number)


def solution(nodeinfo):
    answer = []
    nodes = []
    length_nodeinfo = len(nodeinfo)
    bst = BinarySearchTree()

    for i in range(length_nodeinfo):
        nodes.append((i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    nodes.sort(key=lambda x: x[2], reverse=True)

    for node in nodes:
        n = Node(node[0], node[1])
        bst.insert(n)

    bst.preorder_traversal()
    bst.postorder_traversal()
    answer.append(bst.preorder)
    answer.append(bst.postorder)

    return answer
