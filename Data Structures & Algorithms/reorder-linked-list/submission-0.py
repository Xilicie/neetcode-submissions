# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointers to find middle node
        end, middle = head, head

        while end and end.next:
            middle = middle.next
            end = end.next.next

        # the slow pointer is the middle node
        # now we need to reverse the second half
        prev, curr = None, middle
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # after reversal we have two lists pointing to the middle element at the end
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 <- 4 <- 5
        head1 = head
        head2 = prev
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head2.next = nxt1

            head1 = nxt1
            head2 = nxt2

        if head1:
            head1.next = None
        
        



        
        
        