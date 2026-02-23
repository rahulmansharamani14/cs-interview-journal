You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100



"""
Approach 1: Using length of list
- Compute the length of list in 1 pass
- Find the kth node from start and kth node from end
- Swap Nodes

TC: O(n)
SC: O(1)


Approach 2: Using Two Pointers
- Use a dummyNode to avoid edge cases at the start of the list
- Place both pointers at the gap of k nodes
- Move both pointers at a constant speed
- When the left pointer reaches the kth node from start, right pointer will be automatically at kth node from end
- Swap both nodes

Note: Go till the left's prev and right's prev to do the swap operation

TC: O(n)
SC: O(1)
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def swapNodes(head: ListNode, k: int) -> ListNode:
	
	dummyNode = ListNode(0, head)
	
	# initialize both pointers st start
	left = right = dummyNode
	
	#place both pointers at the gap of k nodes 
	for _ in range(k):
		right = right.next
	
	kth_node_from_start = right
	
	# move both pointers at constant speed untill we reach kth node from start
	while right.next:
		right = right.next
		left = left.next
	
	kth_node_from_end = left.next

	
	#swap both values
	kth_node_from_start.val, kth_node_from_end.val = kth_node_from_end.val, kth_node_from_start.val
	
	return dummyNode.next
	
	