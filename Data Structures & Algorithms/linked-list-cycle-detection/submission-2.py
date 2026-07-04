# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head
        ptr2 = head
        while ptr2 and ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if not ptr2:
                break
            ptr2 = ptr2.next 

            if ptr1 == ptr2:
                return True

        return False