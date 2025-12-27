# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

# Example 1:


# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.
# Example 2:


# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n


# """
# Approach 1: Sort and Compare
# - Pre-build a list from 1 to n in sorted order. 
# - Go through the matrix row by row, sort each row list and compare it woth pre-build sorted list
# - Similarly go Go through the matrix column by column, sort each column list and compare it woth pre-build sorted list

# TC: O(n) to pre-build the sorted list + O(n * nlogn)
# SC: O(n)

# """

# def checkValid(self, matrix: list[list[int]]) -> bool:

#     n = len(matrix)
#     num_list = [i for i in range(1, n + 1)]

#     #row check
#     for i in range(n):
#         if num_list != sorted(matrix[i]):
#             return False

#     #column check
#     for i in range(n):
#         column = []

#         for j in range(n):
#             column.append(matrix[j][i])

#         if num_list != sorted(column):
#             return False

#     return True
    
"""
Approach 2: Using Set
- Travers through the matrix row wise, adding elements to a new set. If the element is already present, return False (Invalid matrix)
- Travers through the matrix column wise, adding elements to a new set. If the element is already present, return False (Invalid matrix)
- At the end, return True (Valid Matrix)

TC: O(n * n) for row traversal + O(n * n) for column traversal ~= O(n * n)
SC: O(n) for extra space using set
"""

# def checkValid(self, matrix: list[list[int]]) -> bool:

#     n = len(matrix)

      # row wise
#     for i in range(n):
#         row_set = set()
#         for j in range(n):
#             if matrix[i][j] in row_set:
#                 return False
#             row_set.add(matrix[i][j])
#         
      
      # column wise
#     for j in range(n):
#         column_set = set()
#         for i in range(n):
#             if matrix[i][j] in column_set:
#                 return False
#             column_set.add(matrix[i][j])
#         

#     return True
    
"""
Approach 3: Using XOR (Not accepted for all test cases)

- Pre-compute the XOR value of 1 to n
- Traverse through the matrix row wise, having a XOR of this row. Check if the row XOR matches with precomputed XOR of 1 to n. If they don't match, return False (Invalid Matrix)
- Traverse through the matrix column wise, having a XOR of this column. Check if the column XOR matches with precomputed XOR of 1 to n. If they don't match, return False (Invalid Matrix)
- At the end, return True (Valid Matrix)

TC: O(n) for computing XOR value +  O(n * n) for row traversal + O(n * n) for column traversal ~= O(n * n)
SC: O(1) as only bunch of variables are used
"""

def checkValid(self, matrix: list[list[int]]) -> bool:
    n = len(matrix)

    xor_value = 0

    for i in range(1, n+1):
        xor_value = xor_value ^ i 


    #row wise
    for i in range(n):
        xor_row = 0
        for j in range(n):
            xor_row = xor_row ^ matrix[i][j]
        if xor_row != xor_value:
            return False
        

    #column wise
    for j in range(n):
        xor_column = 0
        for i in range(n):
            xor_column = xor_column ^ matrix[i][j]
        if xor_column != xor_value:
            return False
        
    
    return True
