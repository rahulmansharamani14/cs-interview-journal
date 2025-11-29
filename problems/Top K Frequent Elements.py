# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
Approach 1: Using Sorted Dict
TC: O(n) for building freq map + O(nlogn) to sort dict (in desc order) based on value ~ O(nlogn)
SC: O(k) for freq map + O(k) to store new sorted dict as list ~ O(k)
"""

# from collections import Counter

# def topKFrequent(nums: list[int], k: int) -> list[int]:


#     counter = Counter(nums)

#     sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

#     res = []
#     for i in range(k):
#         res.append(sorted_counter[i][0])
#     return res


"""
Approach 2: Using Max Heap
let m = no of unique lements
TC: O(n) for building freq map + O(m) to transform into a list + O(m) to transform into max-heap of size m + O(klog m) to process k elements from this heap ~ O(klogm)
SC: O(m) for freq map + O(m) to store heap list + O(m) to store max-heap of size n ~ O(m)
"""

# from collections import Counter
# import heapq

# def topKFrequent(nums: list[int], k: int) -> list[int]:

#     counter = Counter(nums)
#     heap_list = []

    
#     for num, freq in counter.items():
#         heap_list.append((-freq, num))
    
#     heapq.heapify(heap_list)

#     res = []
#     for _ in range(k):
#         freq, num = heapq.heappop(heap_list)
#         res.append(num)
    
#     return res

        
# """
# Approach 3: Using Min Heap
# let m = no of unique lements
# TC: O(n) for counter + O(mlogk) to build min heap of size k + O(k) to process min-heap ~ O(mlogk) ~O(nlogk)
# SC: O(n) for counter + O(k) for min-heap of size k ~ O(n)
# """

# from collections import Counter
# import heapq

# def topKFrequent(nums: list[int], k: int) -> list[int]:

#     counter = Counter(nums)
#     heap = []

    
#     # for num, freq in counter.items():
#     #     heap_list.append((-freq, num))
    
#     for num, freq in counter.items():
#         if len(heap) == k:
#             # pushpop
#             heapq.heappushpop(heap, (freq, num))
#         else:
#             heapq.heappush(heap, (freq, num))

#     # traverse the heap list in reverse order 

#     res = []

#     for i in range(k-1, -1, -1):
#         res.append(heap[i][1])

    
#     return res

"""
Approach 4: Using Bucket Sort
let m = no of unique lements
TC: O(n) for counter + O(n) to build buckets list + O(k) to process k elements ~ O(n)
SC: O(n) for counter + O(n) to store bucket list + O(k) for reseult ~ O(n)
"""

from collections import Counter
import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:

    counter = Counter(nums)

    buckets = [0] * (len(nums) + 1) # buckets list which starts with 0 freq all the way upto k freq

    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)

    # traverse this buckets list in reverse order
    res = []

    for i in range(len(buckets) -1, -1, -1):
        if len(res) == k:
            break
        if buckets[i] != 0:
            for value in buckets[i]:
                res.append(value)
    
    return res





    

