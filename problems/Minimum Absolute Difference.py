# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]


'''
Approach 1: Sorting the input, computing min_difference in one pass and return all the pairs of absolute difference equal to min_difference
TC: O(nlogn + 2n) ~ O(nlogn)
SC: O(n)
'''


# def minAbsDifference(arr: list[int]) -> list[list[int]]:
#     arr.sort() #[1,2,3,4]

#     min_difference = float('inf')

#     res = []

#     for i in range(len(arr) - 1):
#         min_difference = min(min_difference, arr[i + 1] - arr[i])

#     for i in range(len(arr) - 1):
#         if min_difference == arr[i + 1] - arr[i]:
#             res.append([arr[i], arr[i+1]])

#     return res
    
'''
Approach 2: Sorting the input and Using a Hashmap to store all pairs with thier absolute difference
TC: O(nlogn + n)
SC: O(2n)
'''

def minAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()

    diff_map = dict() 
    min_diff = arr[1] - arr[0]

    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]

        if min_diff > diff:
            min_diff = diff


        if diff in diff_map:
            diff_map[diff].append([arr[i], arr[i+1]])
        else:
            diff_map[diff] = [[arr[i], arr[i+1]]]
    


    return diff_map[min_diff]
    




'''
Approach 3: One Pass Solution: Compute 1st pair absolute difference and check if any future aboslute diff is less than this, start the res list from that pair
TC: O(nlogn + n)
SC; O(n)

'''

# def minAbsDifference(arr: list[int]) -> list[list[int]]:
#     arr.sort() #[1,2,3,4]

#     min_difference = arr[1] - arr[0]

#     res = []

#     for i in range(len(arr) - 1):
#         if min_difference == arr[i + 1] - arr[i]:
#             res.append([arr[i], arr[i+1]])
        
#         if min_difference > arr[i + 1] - arr[i]:
#             min_difference = arr[i + 1] - arr[i]
#             res = [[arr[i], arr[i+1]]]


#     return res



arr1 = [4,2,1,3]
print(minAbsDifference(arr1))
arr2 = [1,3,6,10,15]
print(minAbsDifference(arr2))
arr3 = [3,8,-10,23,19,-4,-14,27]
print(minAbsDifference(arr3))
arr4 = [1,5,6,8]
print(minAbsDifference(arr4))