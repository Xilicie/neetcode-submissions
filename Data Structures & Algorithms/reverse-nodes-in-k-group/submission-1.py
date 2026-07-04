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
        result = dummy
        curr = head
        prev = dummy

        while curr:
            counter = 0
            old_head = curr
            # check if the group has enough element to reverse
            temp = curr
            while counter < k and temp:
                temp = temp.next
                counter += 1
            if counter == k:
                counter = 0
                while counter < k:
                    prev, curr = self.reverseGroup(prev, curr)
                    counter += 1

                dummy.next = prev
                dummy = old_head

                old_head.next = curr
                prev = old_head           
            else:
                dummy.next = curr
                break
                


        return result.next
            


