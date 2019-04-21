"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tmp = head
        head.next = tmp
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmp.next = l1
                tmp = l1
                l1 = l1.next
            else:
                tmp.next = l2
                tmp = l2
                l2 = l2.next
        cur = l1
        if l1 == None:
            cur = l2
        while cur != None:
            tmp.next = cur
            tmp = cur
            cur = cur.next
        if head.next == None:
            return None
        return head.next

"""        
执行用时 : 60 ms, 在Merge Two Sorted Lists的Python3提交中击败了79.80% 的用户
内存消耗 : 13.2 MB, 在Merge Two Sorted Lists的Python3提交中击败了53.98% 的用户
"""