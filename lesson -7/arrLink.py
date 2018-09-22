#!coding=utf-8
"""
数组链表：

存储元素个数固定或总数受限，
操作时分为针对链表的next处理，以及针对数组的索引位
head,freelist均为序列值，代表了数组对象序号
"""
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
def addNode(arrLink, head, freelist, Node):
    # 数组链表添加元素,向链表头部添加，但存储在数组的后位
    newElem = freelist # 当前freelist指向的数组空位序号
    freelist = arrLink[freelist].next  # freelist指向下一个数组空位序号
    
    arrLink[newElem].value = Node.value #对空位赋值以及标记next-1标识末尾
    arrLink[newElem].next = -1
    
    if head == -1:
        head = newElem
    else:
        arrLink[newElem].next = head
        head = newElem
    return(head, freelist)

if __name__ == '__main__':
    nodeCount = 10
    ll = [None] * nodeCount
    freelist = 0
    head = -1
    
    # 数据初始
    for i in range(nodeCount):
        ll[i] = Node()
        ll[i].next = i + 1
    ll[nodeCount - 1].next = -1
    freelist = 0
    
    # 添加节点
    head, freelist = addNode(ll, head, freelist, Node("hello")
    
