

# 拼接两个链表，而不增加额外空间复杂度

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)

        if l1 ==None:
            return l2
        elif l2 == None:
            return l1
        if l1.val <= l2.val:
            flag  = 1
            prehead.next = l1
        else:
            flag = 0
            prehead.next =l2
        while l1 and l2:
            if flag:
                if l1.next == None or ( l1.next and l1.next.val>l2.val):
                    next_l1 = l1.next
                    l1.next = l2
                    l1 = next_l1
                    flag = 0
                else:
                    l1 = l1.next
            else:
                if l2.next == None or ( l2.next and l2.next.val > l1.val):
                    next_l2 = l2.next
                    l2.next = l1
                    l2 = next_l2
                    flag = 1
                else:
                    l2 = l2.next
        return prehead.next

def p_list(h):
    while h:
        print(h.val,end=' ')
        h = h.next

if __name__ == "__main__":
    p1 = ListNode(7)
    p2 = ListNode(5)
    p3 = ListNode(6)
    p4 = ListNode(9)
    p2.next = p3
    p3.next = p4
    s = Solution()
    res = s.mergeTwoLists(p1,p2)
    p_list(res)
