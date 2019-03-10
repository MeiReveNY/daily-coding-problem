def number_of_nodes(tree=list()):

  if not isinstance(tree, tuple):
    return 1
  elif isinstance(tree, tuple) and len(tree)==0:
    return 0
  else:
    node, left, right = tree
    return 1 + number_of_nodes(right) + number_of_nodes(left)

#Tests

assert number_of_nodes() == 0
assert number_of_nodes((1, 2, 3)) == 3
assert number_of_nodes((1, (3, 4, 5), (1,3, 4))) == 7

# Object oriented solution

class Node:
    def __init__(self):
        self.left = None
        self.right = None


def count_nodes(root, lspine=0, rspine=0):
    if not root:
        return 0

    if not lspine:
        node = root
        while node:
            node = node.left
            lspine += 1
    if not rspine:
        node = root
        while node:
            node = node.right
            rspine += 1

    if lspine == rspine:
        return 2**lspine - 1

    return 1 + \
        count_nodes(root.left, lspine=lspine-1) + \
        count_nodes(root.right, rspine=rspine-1)


# Tests
a = Node()
b = Node()
c = Node()
a.left = b
a.right = c
assert count_nodes(a) == 3
d = Node()
b.left = d
assert count_nodes(a) == 4
e = Node()
b.right = e
assert count_nodes(a) == 5
f = Node()
c.left = f
assert count_nodes(a) == 6
