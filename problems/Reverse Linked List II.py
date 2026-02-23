#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4,5], left = 2, right = 4
#Output: [1,4,3,2,5]
#Example 2:
#
#Input: head = [5], left = 1, right = 1
#Output: [5]
# 
#
#Constraints:
#
#The number of nodes in the list is n.
#1 <= n <= 500
#-500 <= Node.val <= 500
#1 <= left <= right <= n
# 
#
#Follow up: Could you do it in one pass?

"""

Approach 1: Using a Stack:
- Traverse through the left's prev node
- Push the elements onto the stack untill the right node
- Pop out elements from the stack in reversed manner, attaching back to the existing list

TC: O(n)
SC: O(right - left) ~ constant space

Approach 2: Using In-Place Reversal
- Find the left and right node
- Detach the list (left to right) from the original list
- Reverse the detached list
- Attach the reversed list to original list

TC: O(n)
SC: O(1)

"""

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:

	def _reverse_list(head: ListNode) -> ListNode:
		prev = None
		curr = head
		
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev
		
	if not head or left == right:
		return head
	
	dummyNode = ListNode(0, head)
	curr = dummyNode

	#find left_node
	for _ in range(1, left):
		curr = curr.next
	
	left_node_prev = curr
	left_node = left_node_prev.next
	
	#find right_node
	for _ in range(left, right + 1):
		curr = curr.next
		
	right_node = curr
	right_node_next = curr.next
		
	#break the list
	left_node_prev.next = None
	right_node.next = None
	
	#reverse in-between
	new_head = _reverse_list(left_node)
	
	#connect the reversed list to existing list
	left_node_prev.next = new_head
	left_node.next = right_node_next
		
	return dummyNode.next
	
	

