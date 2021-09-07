from collections import Counter
from heapq import heapify, heappop, heappush
from string import hexdigits


class Node:
    def __init__(self, letter=None, freq=0, children=None):
        self.letter = letter
        self.freq = freq
        self.children = children or []

    def tuple(self):
        return (self.freq, ord(self.letter) if self.letter else -1)

    def __lt__(self, other):
        return self.tuple() < other.tuple()

    def __eq__(self, other):
        return self.tuple() == other.tuple()


def encoding_table(node, code=''):
    if node.letter is None:
        mapping = {}
        for child, digit in zip(node.children, hexdigits):
            mapping.update(encoding_table(child, code + digit))
        return mapping
    else:
        return {node.letter: code}


def huffman_encode(text):
    nodes = [Node(letter, freq) for letter, freq in Counter(text).items()]
    heapify(nodes)

    while len(nodes) > 1:
        list_children = [heappop(nodes) for _ in range(2)]
        freq = sum([node.freq for node in list_children])

        node = Node(None, freq)
        node.children = list_children

        heappush(nodes, node)

    root = nodes[0]
    codes = encoding_table(root)

    return ''.join([codes[letter] for letter in text])


print(huffman_encode('abcdefghijklmnop'))
