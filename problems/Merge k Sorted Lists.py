#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
#Merge all the linked-lists into one sorted linked-list and return it.
#
# 
#
#Example 1:
#
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted linked list:
#1->1->2->3->4->4->5->6
#Example 2:
#
#Input: lists = []
#Output: []
#Example 3:
#
#Input: lists = [[]]
#Output: []
# 
#
#Constraints:
#
#k == lists.length
#0 <= k <= 104
#0 <= lists[i].length <= 500
#-104 <= lists[i][j] <= 104
#lists[i] is sorted in ascending order.
#The sum of lists[i].length will not exceed 104.

"""
Approach: Using Heaps (priority queue)

TC: O(n * log k)
SC: O(k)
"""

import heapq

class ListNode:
	def __init__(self, val= 0, next= None):
		self.val = val
		self.next = next


def mergeKLists(lists: list[ListNode]) -> ListNode:

	if not lists: return None
	
	heap = []
	
	# build heap: add k elements to heap -> (k * log k)
	for i in range(len(lists)):
		head = lists[i]
		
		if head:
			heapq.heappush(heap, (head.val, i, head))
	
	dummy = ListNode(0)
	curr = dummy
	
	# (n * log k)
	while heap:
		val, i, node = heapq.heappop(heap)
		curr.next = node
		curr = node
		node = node.next
		
		if node:
			heapq.heappush(heap, (node.val, i, node))
	
	# return new head
	return dummy.next

