#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        current = head
        fakePre = ListNode(0)
        fakePre.next = head
        while current:
            currentNext = current.next
            current.next = None
            pre = fakePre
            now = pre.next
            while now != current and now != None:
                if now.val >= current.val:
                    pre.next = current
                    current.next = now
                    break
                pre = now
                now = now.next
            if now == None:
                pre.next = current

            current = currentNext
        return fakePre.next
s = Solution()
h = ListNode(4)
h.next = ListNode(2)
h.next.next = ListNode(1)
h.next.next.next = ListNode(3)
h.next.next.next.next = ListNode(5)
r = s.insertionSortList(h)
while r:
    print(r.val)
    r = r.next