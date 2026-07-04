"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        hashMap = {None : None}
        while ptr:
            copy = Node(ptr.val)
            hashMap[ptr] = copy
            ptr = ptr.next

        i = head
        while i:
            copy = hashMap[i]
            copy.next = hashMap[i.next]
            copy.random = hashMap[i.random]
            i = i.next

        return hashMap[head]
