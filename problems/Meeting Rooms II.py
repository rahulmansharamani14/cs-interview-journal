# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1


# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106


"""
Approach 1: Using Priority Queus (Min- Heap)

TC: O(nlogn) for sorting + O(nlogn) for traversing through the interval list and inserting into heap ~= O(nlogn)
SC: O(n) for heap size in worst case
"""

import heapq


def minMeetingRooms(intervals: list[list[int]]) -> int:

    intervals.sort(key=lambda x: x[0])

    heap = []
    heapq.heappush(heap, intervals[0][1])  # adding th first meeting

    for i in range(1, len(intervals)):
        end_time = intervals[i][1]

        if (
            heap[0] > intervals[i][0]
        ):  # top element (current end_time) > next meeting start_time
            heapq.heappush(heap, end_time)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, end_time)

    return len(heap)
