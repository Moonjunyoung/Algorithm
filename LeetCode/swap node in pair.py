class Solution:
    def swap_node(self, li: ListNode, cur):
        if li == None:
            return
        
        # 1. 맨 마지막 노드일떄  
        if li.next == None:
            # 1.2 전체노드의 개수가 짝수개면 마지막값반환
            if cur % 2 == 0:
                return str(li.val)
            # 1.3 홀수개면 반환 x
            else:
                return None
        else:
            a = self.swap_node(li.next, cur + 1)
            if a == None:
                return li.val
            else:
                tmp = str(li.val)
                li.next.val = tmp
                li.val = a
                return None

        return

    def swapPairs(self, head: ListNode) -> ListNode:
        self.swap_node(head, 1)

        return head