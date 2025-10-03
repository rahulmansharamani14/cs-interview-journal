# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Initial Thoughts/Questions:
# How big is this stream can be? In the range of?

# Approach:
# We can define a list of integers as stream. maintaining it's running sum and it's length.
# To find median, we just need to check if the length of stream is even/odd. If it's odd, we just simply return the middle value as we have the index of the middle value.
# if it's even, then we just need to get two middle value and retuirn it's average/mean
#
# TC: O(nlogn)
# SC: O(len(stream))



# class MedianFinder():
#     """Find Median of all the elements in the Data stream"""
#     def __init__(self):
#         self.stream: list[int] = []

#     def addNum(self, num: int):
#         self.stream.append(num)

#     def findMedian(self) -> float:
#         self.stream.sort()
#         # If the stream length is even, compute mean of two middle values
#         if len(self.stream) % 2 == 0:
#             mid1 = len(self.stream) // 2 - 1
#             mid2 = len(self.stream) // 2
#             median = (self.stream[mid1] + self.stream[mid2]) / 2
#         else:
#             # If the stream length is odd, compute middle value
#             middle_index = len(self.stream)// 2
#             median = self.stream[middle_index]
#         return median




# [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
# 6 + 10 + 2 + 6 + 5 + 0 + 6 + 3 + 1 + 0 + 0 = 39 / 11 = 3.5454


# Approach 2: Using Priority Queue/Heap
# We can use a priority queue to store all the elements of the stream that give O(logn) insertime time and the stream elements
# will be in sorted order. If the len(stream) is odd, we simply return the middle value Else we return the averge of both the middle values.ArithmeticError
#
# TC: O(log n)
# SC: O(len(n)) where n is nof of elements in the stream
#

import heapq

class MedianFinder():
    """Find Median of all the elements in the Data stream"""
    def __init__(self):
        self.stream: list[int] = []

    def addNum(self, num: int):
        heapq.heappush(self.stream, num) #Using heap to maintain sorted order of elements

    def findMedian(self) -> float:
        if len(self.stream) % 2 != 0:
            mid_value = self.stream[len(self.stream) // 2]
            median = self.stream[mid_value]
        else:
            mid1 = self.stream[len(self.stream) // 2 - 1]
            mid2 = self.stream[len(self.stream) // 2]
            median = (mid1 + mid2) / 2
        return median

def run_tests():
    #Happy case
    m1 = MedianFinder()
    m1.addNum(1)
    m1.addNum(2)
    test(1.5, m1.findMedian())
    m1.addNum(3)
    test(2.0, m1.findMedian())
    m1.addNum(4)
    test(2.5, m1.findMedian())
    m2 = MedianFinder()
    m2.addNum(6)
    assert 6.00 == m2.findMedian()
    m2.addNum(10)
    assert 8.00 == m2.findMedian()
    m2.addNum(2)
    assert 6.00 == m2.findMedian()
    m2.addNum(6)
    assert 6.00 == m2.findMedian()
    m2.addNum(5)
    assert 6.00 == m2.findMedian()
    m2.addNum(0)
    assert 5.50 == m2.findMedian()
    m2.addNum(6)
    assert 6.00 == m2.findMedian()
    m2.addNum(3)
    assert 5.50 == m2.findMedian()
    m2.addNum(1)
    assert 5.00 == m2.findMedian()
    m2.addNum(0)
    assert 4.00 == m2.findMedian()
    m2.addNum(0)
    assert 3.00 == m2.findMedian()
    print("All tests passed")

def test(expected, result):
    assert expected == result, f"findMedian: expected: {expected}, got: {result}"

if __name__ == "__main__":
    run_tests()
