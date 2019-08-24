#!./env python

from collections import defaultdict

class Node:
    def __init__(self, t, attr='', i=0, count=1):
        self.t = t
        self.attr = attr
        assert(isinstance(i, int) and i>=0), (type(i), i)
        self.i = i
        # identidication properties
        self.tup_ = (self.t, self.attr, self.i)

        # other properties
        self.count = count
        self.neighbors = defaultdict(lambda: defaultdict(Node))

    def __str__(self):
        # if self.i > 0:
        #     return '%s%i(%s)' % (self.t, self.i, self.attr)
        # return '%s(%s)' % (self.t, self.attr)
        if self.i > 0:
            return '%s%i' % (self.t, self.i)
        return '%s' % self.t

    def __eq__(self, other):
        """
        must implement this to support comparation between nodes
        """
        if not isinstance(other, Node):
            raise TypeError((other, type(other)))
        # return self.t == other.t and self.attr == other.attr and self.i == other.i
        return self.tup_ == other.tup_

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise TypeError((other, type(other)))
        # return self.t < other.t or (self.t == other.t and self.attr < other.attr)
        return self.tup_ < other.tup_

    def __hash__(self):
        """
        need to explicitly implement hash function to make it hashable if __eq__ is implemented
        seems to recommend xor.
           see. https://stackoverflow.com/questions/4005318/how-to-implement-a-good-hash-function-in-python
                https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash
        """
        # return hash((self.t, self.attr))
        return hash(self.tup_)

    def __repr__(self):
        if self.i > 0:
            return '%s%i(%s)' % (self.t, self.i, self.attr)
        return '%s(%s)' % (self.t, self.attr)
        # return self.__str__()

    def _reset(self):
        """
        discard id
        """
        return Node(self.t, attr=self.attr)
