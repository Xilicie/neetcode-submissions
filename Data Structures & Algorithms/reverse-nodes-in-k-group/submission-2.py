# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, prev, curr):
        next_tmp = curr.next
        curr.next = prev

        return curr, next_tmp
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy
        curr = head

        while True:
            temp = curr
            count = 0
            while count < k and temp:
                temp = temp.next
                count += 1

            if count != k:
                break

            old_head = curr
            prev = None
            for _ in range(k):
                prev, curr = self.reverseGroup(prev, curr)

            group_prev.next = prev
            group_prev = old_head
            old_head.next = curr
        
        old_head.next = curr
        
        return dummy.next
        


        

