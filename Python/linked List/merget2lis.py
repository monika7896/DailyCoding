class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# l1 =1,2,3, l2=1,2,4
class Solution:
    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(5)

solution = Solution()
result = solution.mergeTwoList(l1, l2)

# Print the result
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
