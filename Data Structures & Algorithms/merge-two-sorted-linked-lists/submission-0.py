# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a placeholder dummy node to build the list on
        dummy = ListNode()
        current = dummy
        
        # Traverse while both lists have remaining elements
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Append the remaining nodes from whichever list is left over
        current.next = list1 if list1 else list2
        
        # Return the actual head of the merged list, bypassing the dummy
        return dummy.next
