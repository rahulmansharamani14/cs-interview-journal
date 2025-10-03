import time

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# - void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# - String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"

# Initial Thoughts/Clarifying Questions:
# Is this timestamp is considered as int for this problem os something else?
# How many possible different values can be stored for the same key? Is their an upper cap?
#
# Approach 1: we can build a custom data structure (hashmap) with unique key and a list of values for each unique key. This list will
# further contian a tuple/sublist to store (val, timestamp).
#
# TC: set(): O(1); get(): O(log n) where n is the size of value list
# SC: O(set calls)
# Code:
#

class TimeMap:
    """Time Based Key Value Store"""
    def __init__(self):
        self.time_map: dict = {}

    def set(self, key: str, value: str, timestamp: int):
        """Stores the key with a value ata given timestamp  """
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key:str, timestamp: int) -> str:
        """Returns a value at a given timestamp"""
        if not key in self.time_map: #Checks if the key is not present
            return ""

        if len(self.time_map[key]) == 0: #Checks if there are no values for this key
            return ""

        if timestamp < self.time_map[key][0][0]:
            #Checks if given timestamps is less than the 1st timestamps (since timestamps are in stricly increasing order)
            return ""

        all_values = self.time_map[key]
        #use binary search to get the value
        left, right = 0, len(all_values) - 1
        ans = ""
        while left <= right:
            mid = (left + right)// 2

            if all_values[mid][0] <= timestamp:
                ans = all_values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans


def main():
    timeMap = TimeMap()
    timeMap.set("foo","bar", 1)
    assert timeMap.get("foo", 1) == "bar"
    assert timeMap.get("foo", 3) == "bar"
    timeMap.set("foo","bar2", 4)
    assert timeMap.get("foo", 4) == "bar2"
    assert timeMap.get("foo", 5) == "bar2"

    print("All test cases passed")

main()
