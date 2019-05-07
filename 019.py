
# 删除链表中倒数第n个节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head
        first , second = prehead ,prehead
        while n-1:
            first = first.next 
            n -=1
        while first.next != None:
            first = first.next
            preSecond = second
            second = second.next
        preSecond.next = preSecond.next.next
        return prehead.next
    
