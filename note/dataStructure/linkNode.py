#coding=utf-8

class Node(object):
    def __init__(self, value=None, nextP=None):
        self.value = value
        self._next = nextP

    def __repr__(self):
        return str(self.value)

class LinkNode(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, node):
        if not isinstance(node):
            node = Node(node)
        nd = self.head
        if self.head:
            while nd._next:
                nd = nd._next
            nd._next = node
        else:
            self.head = node
        self.length += 1

if __name__ == '__main__':
    string = "hello"
    linkNode = LinkNode()
    
    for s in string:
        nd = Node(s)
        linkNode.append(nd)


