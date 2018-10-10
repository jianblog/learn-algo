#coding=utf-8
"""
单向链表字符串，判断是否为回文，即正反相同

方法1：对单向链表使用两个指针，分别以间距1步，2步进行遍历，
       当p2达到终点时，p1位置为中间点

注解1：字符串为奇偶长度，比较上有区别
      奇数abcba时，p2最终位于a元素，p1为c, 这种情况再将p1前进一步
      偶数abba时，p2最终为空,p1为第二个b
"""
import sys

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self._next = None

    def __repr__(self):
        return str(self.value)

class LinkNode(object):
    def __init__(self):
        self.head = None

    def add(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        nd = self.head
        if self.head:
            while nd._next:
                nd = nd._next
            nd._next = node
        else:
            self.head = node

def isPalindrome(linkword):
        
    p1 = linkword.head
    p2 = linkword.head
    arr = [] # 额外使用空间保存单链表遍历的上半部分
    
    while p2 and p2._next:
        arr.append(p1)
        p1 = p1._next  # p1 一步
        p2 = p2._next._next  # p2 两步
    if p2:
        # 注解1
        p1 = p1._next
    
    # 当前p1位于单链表中位
    #print(arr, p1.value)
    while p1:
        tmp = arr.pop()
        if not p1.value == tmp.value:
            print("not same --",p1.value, tmp.value)
            print("It's not a Palindrome.")
            return -1
        p1 = p1._next
    print("It's a Palindrome!")
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        #strings = "helloolleh"
        linkword = LinkNode()
        for s in sys.argv[1]:
            linkword.add(Node(s))
        isPalindrome(linkword)


