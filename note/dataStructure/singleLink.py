# coding = utf-8

import links

def reverse(single_link):
    """
    单向链表翻转操作
    """
    if not single_link.head or not single_link.head._next:
        return single_link
    last = single_link.head
    cur  = last._next
    last._next = None
    while cur._next:
        front = cur._next
        cur._next = last
        
        last = cur
        cur = front
    cur._next = last
    single_link.head = cur
    return single_link


if __name__ == '__main__':
    strings = "wonderful"
    single_link = links.NodeLink()
    for s in strings:
        single_link.add(links.Node(s))

    links_reverse = reverse(single_link)

    # 遍历打印链表
    head = links_reverse.head
    while head:
        print(head.value)
        head = head._next


