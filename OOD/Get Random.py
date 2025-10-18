# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

# Constraints:

# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

import random

class RandomizedSet():
    def __init__(self):
        self.index_map = dict()
        self.random_list = []
        

    def insert(self, val : int) -> bool:
        if val in self.index_map:
            return False
        
        self.random_list.append(val)
        self.index_map[val] = len(self.random_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        val_index = self.index_map[val]

        #swap the last element with the curr element and then remove the last element
        last_element, curr_element = self.random_list[-1], self.random_list[val_index]
        self.random_list[val_index], self.random_list[-1] = last_element, curr_element
        
        self.index_map[last_element] = val_index #updating the index of last element in dict

        self.random_list.pop() # removing the last element from list
        del self.index_map[val] # removing the key from dict
        

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.random_list) - 1)
        return self.random_list[random_index]


# random_list = 

# index_map = {

# }


# Explanation
randomizedSet = RandomizedSet()
print(randomizedSet.remove(0))
#  Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(0))
# // Returns false as 2 does not exist in the set.
print(randomizedSet.insert(0))
# // Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom())
# // getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(0))
# // Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(0))
# // 2 was already in the set, so return false.
# print(randomizedSet.getRandom())
# // Since 2 is the only number in the set, getRandom() will always return 2.