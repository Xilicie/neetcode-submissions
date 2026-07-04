# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                res.append(node.val) 
                node = node.next
        res.sort()
        dummy = ListNode()
        cur = dummy
        for i in range(len(res)):
            val = res[i]
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next
            
        