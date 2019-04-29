
# 两个链表数相加

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        remind = head
        copy_l1, copy_l2 = l1, l2
        n_num = 0
        while copy_l1 or copy_l2 or n_num:
            if copy_l1:
                temp_1 = copy_l1.val
                copy_l1 = copy_l1.next
            else:
                temp_1 = 0
            if copy_l2:
                temp_2 = copy_l2.val
                copy_l2 = copy_l2.next
            else:
                temp_2 = 0
            
            temp = temp_1 + temp_2 + n_num
            n_num = temp //10 
            current  = temp % 10

            remind.val = current
            if copy_l2 or copy_l1 or n_num:
                remind.next = ListNode(0)
                remind = remind.next
        return head
            

def print_list(l):
    while l !=None:
        print(l.val)
        l = l.next
if __name__ == "__main__":
    S = Solution()
    head = ListNode(9)
    head.next = ListNode(9)

    r = S.addTwoNumbers(ListNode(1),head)
    print_list(r)
