"""
Questions:

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.


Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3



Initial Thoughts/Questions:
- how is this stream of integers are represented in the input? Is it a list?
- how big this size can be?


Code:

Approach 1:
"""


# class MovingAverage:
# 	def __init__(self, size: int):
# 		self.size = size
# 		self.stream: list[int] = []
# 		self.stream_length = 0

# 	def next(self, val: int) -> float:
# 		self.stream.append(val)
# 		self.stream_length += 1
# 		return self.calculate_moving_average()


# 	def calculate_moving_average(self):
# 		if self.stream_length < self.size:
# 			p1 = 0
# 			window_size = self.stream_length
# 		else:
# 			p1 = self.stream_length - self.size
# 			window_size = self.size

# 		p2 = self.stream_length - 1

# 		window_sum = 0
# 		while p1 <= p2:
# 			window_sum  += self.stream[p1]
# 			p1 += 1

# 		moving_average = window_sum / window_size
# 		return moving_average


# # Test

# movingAverage = MovingAverage(3)
# assert 1.0 == movingAverage.next(1)
# assert 5.5 == movingAverage.next(10)
# assert 4.66667 == movingAverage.next(3)
# assert 6.0 == movingAverage.next(5)



"""
Approach 2: Using Queue (fixed size) to track all the stream integers with running sum (O(1))

TC: O(1)
SC: O(size)

"""

from collections import deque

class MovingAverage:
    """Moving avergae of the last size window of the stream"""
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be greater than 0")
        self.size: int = size
        self.stream: deque = deque()
        self.stream_running_sum = 0

    def next(self, val: int) -> float:

        # Check if stream queue is full
        if len(self.stream) >= self.size:
            removed_val = self.stream.popleft()
            self.stream_running_sum -= removed_val

        self.stream.append(val) # Add next value to the stream
        self.stream_running_sum += val #Updating running sum
        moving_average = self.stream_running_sum / len(self.stream)
        return moving_average


# Tests



def run_tests():
    # Happy Case (given example)
    m1 = MovingAverage(3)
    assert 1.00 == m1.next(1);
    assert 5.5 == m1.next(10);
    assert 4.66667 == m1.next(3);
    assert 6.0 == m1.next(5);


    #Edge Case
    m2 = MovingAverage(0)
    assert m2.next(5)

if __name__ == "__main__":
    run_tests()
