class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        hd2 = slow.next
        prev = slow.next = None
        while hd2:
            temp = hd2.next
            hd2.next = prev
            prev = hd2
            hd2 = temp
        
        l, r = head, prev
        while r:
            tmp1 = l.next
            tmp2 = r.next
            l.next = r
            r.next = tmp1
            l = tmp1
            r = tmp2