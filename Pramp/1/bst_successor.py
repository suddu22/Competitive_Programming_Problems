"""
An in order successor is the smallest key that is greater than n's key.
Let's call n's in-order successor in the tree s

We discern between 2 cases:

Node n has a right child: in this case s is the node with the minimum key on n's right sub-tree.
Node n doesn't have a right child: in this case s is one of n's ancestors. More specifically, within n's ancestor chain (starting from n up to the root), s is the first parent that has a left child on that chain.

If n doesn't have a right child and all of its ancestors are right children to their parents, n doesn't have a successor (s is null).

O(h)
where h is the height of the tree > O(log n)

"""


class BSTNode(object):
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.right = None
        self.left = None
        self.size = 1

    def update_size(self):
        r = (0 if self.left is None else self.left.size)
        l = (0 if self.right is None else self.right.size)
        return r + l

    def insert(self, t):
        self.size += 1

        if t < self.key:
            if self.left is None:
                self.left = BSTNode(t)
                return self.left
            else:
                return self.left.insert(t)
        else:
            if self.right is None:
                self.right = BSTNode(t)
                return self.right
            else:
                return self.right.insert(t)

    def find(self, t):
        if t == self.key:
            return self
        elif t < self.key:
            if self.left is None:
                return None
            return self.left.find(t)
        else:
            if self.right is None:
                return None
            return self.right.find(t)

    def rank(self, t):
        left_size = (0 if self.left is None else self.left.size)
        if t == self.key:
            return left_size + 1
        elif t < self.key:
            if self.left is None:
                return 0
            else:
                return self.left.rank(t)
        else:
            if self.right is None:
                return left_size + 1
            else:
                return self.right.rank(t) + left_size + 1

    def getMin(self, current):
        while current.left is not None:
            current = current.left
        return current

    def successor(self):
        if self.right is not None:
            return self.right.minimun()
        else:
            current = self
            parent = current.parent
            while parent is not None and parent.right is current:
                current = parent
                parent = parent.parent
            return parent
