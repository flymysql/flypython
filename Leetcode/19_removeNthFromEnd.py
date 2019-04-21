"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 辅助数组法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        h = head
        tmp = []
        while h != None:
            tmp.append(h)
            h = h.next
        if tmp[-n] == tmp[0]:
            return tmp[1]
        if tmp[-n].next == None:
            tmp[-n-1].next = None
        else:
            tmp[-n-1].next = tmp[-n+1]
        return head
    
    # 双指针法
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        h1 = head
        h2 = head
        for _ in range(n):
            h2 = h2.next
        if h2 == None:
            return head.next
        while h2.next != None:
            h1 = h1.next
            h2 = h2.next
        h1.next = h1.next.next
        return head

"""
执行用时 : 52 ms, 在Remove Nth Node From End of List的Python3提交中击败了87.90% 的用户
内存消耗 : 13.2 MB, 在Remove Nth Node From End of List的Python3提交中击败了45.29% 的用户
"""