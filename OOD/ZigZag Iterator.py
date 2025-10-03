# Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

# Implement the ZigzagIterator class:

# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element.


# Example 1:

# Input: v1 = [1,2], v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
# Example 2:

# Input: v1 = [1], v2 = []
# Output: [1]
# Example 3:

# Input: v1 = [], v2 = [1]
# Output: [1]

# Initial Thought/Clarifying Questions:
# Basically we need to output the result in zig zag fashion with both input vectors provided.
# Can these both vectors be empty? in that case an empty array would be ans
# Do these vectors contains duplicates? I don't think it matters if they do as we are prcoessing elements alternatively irrespective of this case, right?
# Do we suppose to return the output in a new array?
# One assumption I'm making that .next() would be only called if applicable (contains elements).
#
# Approach 1: We can use two pointer approach placed at the start of both vectors, alternatively precessing elements and moving forward until we process all elements.
# We also need to check if any of the vector still has some remaining elements to process, if they do we process that as well. For this, we can maintain the curr_index for each vector
# and the curr_vec to see which vector's turn is to return the element.
#
# TC: O(1)  for each hasNext() and next() call
# SC: O(1)  for each hasNext() and next() call
#
# Approach 2: Using Queues of Pointers: We will maintain a queue of vectors along with their curr_index pointers
# which will maintain the order of all the vectors through which we ned to return the value. Also, it would automatically
# take care if processing of any vector is finished.
#
# TC: Every next call will take O(1)
# SC: O(total number of vectors)

from collections import deque

class ZigzagIterator():
    def __init__(self, v1: list[int], v2: list[int]):
        self.vectors: list[list[int]] = [v1, v2]
        self.queue: deque[tuple[list[int], int]] = deque()

        # Initializing the queue with all given non-empty vectors along with the current_index = 0
        for vector in self.vectors:
            if len(vector) != 0:
                self.queue.append((vector, 0))

    def hasNext(self) -> bool:
        return len(self.queue) != 0

    def next(self) -> int:
        vector, index = self.queue.popleft() # Access the front of the queue
        next_value = vector[index]

        # Storing the vector along with it's next index if non-empty
        if index + 1 < len(vector):
            self.queue.append((vector, index + 1))

        return next_value


def tests():
    v1 = [1,2]
    v2 = [3,4,5,6]
    zigzagIterator = ZigzagIterator(v1, v2)
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 1
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 3
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 2
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 4
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 5
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 6
    assert zigzagIterator.hasNext() == False

    v3 = []
    v4 = [2]
    zigzagIterator = ZigzagIterator(v3, v4)
    assert zigzagIterator.hasNext() == True
    assert zigzagIterator.next() == 2
    assert zigzagIterator.hasNext() == False

    print("All tests passed")



if __name__ == "__main__":
    tests()
