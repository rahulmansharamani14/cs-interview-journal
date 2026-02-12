# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true


# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106

"""
Approach 1: Sort the intervals based on start time and check for overlapping
TC: O(nlogn) for sorting
SC: O(n) for extra space for python sorting
"""


def canAttendMeetings(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True
