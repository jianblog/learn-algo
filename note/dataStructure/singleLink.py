# coding = utf-8

import links

def reverse(single_link):
    """
    单向链表翻转操作
    """
    if not single_link.head or not single_link.head._next:
        return single_link
    prev = single_link.head
    cur  = prev._next
    prev._next = None
    while cur._next:
        front = cur._next
        cur._next = prev 
        
        prev = cur
        cur = front
    cur._next = prev
    single_link.head = cur
    return single_link

def isPalindrome(single_link):
    """
    单链表判断是否回文串:正反内容相同

    注解1：字符串为奇偶长度，比较上有区别
      奇数abcba时，p2最终位于a元素，p1为c, 这种情况再将p1前进一步
      偶数abba时，p2最终为空,p1为第二个b
    """
    p1 = single_link.head
    p2 = single_link.head
    arr = [] # 使用额外空间存储单链表上半部分
    
    while p2 and p2._next:
        arr.append(p1)
        p1 = p1._next  # p1 一步
        p2 = p2._next._next # p2 两步
    if p2:
        # 注解1
        p1 = p1._next
        
    # p1位于单链表中位, 与保存于arr中的进行比较
    while p1:
        tmp = arr.pop()
        if not p1.value == tmp.value:
            print("It's not a Palindrome.")
            return -1
        p1 = p1._next
    print("Great, it's a Palindrome!")

def checkLoop(single_link):
    if not single_link.head or not single_link.head._next:
        return
    p1 = single_link.head
    p2 = single_link.head
    while p1._next and p2._next:
        p1 = p1._next
        p2 = p2._next._next
        if id(p1) == id(p2):
            print("loops!")
            return -1

if __name__ == '__main__':
    strings = "wonderednow"
    single_link = links.NodeLink()
    for s in strings:
        single_link.add(links.Node(s))

    #links_reverse = reverse(single_link)

    isPalindrome(single_link)

    # 遍历打印链表
    head = single_link.head
    while head:
        print(head.value)
        head = head._next


