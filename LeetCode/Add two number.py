class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reversed_node(self,li:ListNode):
        if li.next==None:
            return str(li.val)
        else:
            return self.reversed_node(li.next)+str(li.val)


        return
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=self.reversed_node(l1)
        b=self.reversed_node(l2)
        answer=(str(int(a)+int(b)))
        
        head=None
        for i in reversed(answer):
           if not head:
                head=ListNode(int(i))
                n=head
           else:
                n.next=ListNode(int(i))
                n=n.next
           
        return head