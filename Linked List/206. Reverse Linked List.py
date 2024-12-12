# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
# Time: O(n)
# Space: O(1)