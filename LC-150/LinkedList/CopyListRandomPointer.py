class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None : None}
        curr = head

        while curr:
            copyNode = Node(curr.val)
            hashmap[curr] = copyNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = hashmap[curr]
            copyNode.next = hashmap[curr.next]
            copyNode.random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]