#coding=utf-8

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class NodeLink(object):
  def __init__(self):
    # 链表类的head属性指向第一个节点
    self.head = None

  def add(self, node): 
    if self.head:
      head = self.head
      while head.next:
        head = head.next
      head.next = node
    else:
      self.head = node
