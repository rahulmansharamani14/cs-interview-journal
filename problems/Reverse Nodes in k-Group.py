#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
#Example 2:
#
#
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
# 
#
#Constraints:
#
#The number of nodes in the list is n.
#1 <= k <= n <= 5000
#0 <= Node.val <= 1000
# 
#
#Follow-up: Can you solve the problem in O(1) extra memory space?



"""
Approach 1: Using Stack 
- Push every k nodes onto the stack 
- Pop these k nodes in revered manner and attach these nodes to the existing list
- Repeat above steps untill there are less than k nodes in the list

TC: O(n)
SC: O(k) 

Approach 2: In-place Reversal of each k nodes
- For every k nodes, reverse the mini-list in-place
- Attach this reversed mini-list to the existing list
- Repeat above steps untill there are less than k nodes in the list

TC: O(n)
SC: O(1)
"""

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next= next

def reverseKGroup(head: ListNode, k: int) -> ListNode:

	dummyNode = ListNode(0, head)
	
	def _reverse_list(head: ListNode) -> ListNode:
		prev = None
		curr = head
		
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev
	
	def _getKthNode(node: ListNode, k) -> ListNode:
		curr = node
		
		while curr and k > 1:
			curr = curr.next
			k -= 1
		return curr
	
	group_prev = dummyNode
	
	while group_prev:
		
		group_head = group_prev.next
		kth_node = _getKthNode(group_head, k)
		
		# check if we have >= k elements
		if not kth_node:
			break
			
		group_next = kth_node.next
		
		#detach the group
		group_prev.next = None
		kth_node.next = None
		
		#reverse the group
		new_group_head = _reverse_list(group_head)
		
		#attach the reversed list to original list
		group_prev.next = new_group_head
		group_head.next = group_next
		
		#move to the next group
		group_prev = group_head
	
	return dummyNode.next
		