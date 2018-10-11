# coding=utf-8
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self._next = None

    def __repo__(self):
        return str(self.value)

class NodeLink(object):
    def __init__(self):
        self.head = None
    def add(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        nd = self.head
        if nd:
            while nd._next:
                nd = nd._next
            nd._next = item 
        else:
            self.head = item
