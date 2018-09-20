#coding=utf-8

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class NodeLink(object):
  def __init__(self):
    # 链表类的head指向链表第一个节点
    self.head = None

  def add(self, node): 
    if self.head:
      head = self.head
      while head.next:
        head = head.next
      head.next = node
    else:
      self.head = node  


def reverse(node):
  """
  逆序方法：
  1. 只要node有下一节点，则递归遍历node.next.边界条件为next为空
  2. 最终递归到尽头时得到末尾节点返回作为新的newHead
  3. node.next.next两个语句最先改变的是原链表末尾元素的next属性，依次从嵌套中返回时逐个倒着改变了各节点的next指向
  """
  if not node.next:
    return node
  newHead = reverse(node.next)
  
  node.next.next = node
  node.next = None
  
  return newHead
  
  if __name__ == "__main__":
    a = Node("we")
    b = Node("are")
    c = Node("all")
    d = Node("world")

    lx = NodeLink()
    lx.add(a)
    lx.add(b)
    lx.add(c)
    lx.add(d)
    
    m = reverse(lx.head)
