class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        ptr1 = dummy
        ptr2 = head 

        for i in range(n):
            ptr2 = ptr2.next

        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = ptr1.next.next

        return dummy.next