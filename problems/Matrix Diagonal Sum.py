# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 
# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

# Example 2:

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:

# Input: mat = [[5]]
# Output: 5
 

# Constraints:

# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100



"""

Approach:
- Primary Diagonal can be accessed by [i,i] going from top left to bottom right
- Secondary Diagonal can be accessed by [i, len(mat) - i - 1] from top right to bottom left (decrementing j index everytime by 1)
- For odd length matrix, they cross each other and middle value is added 2 times, so subtract one time from the total sum
- For even length matrix, they do not cross each other (no need to do anything).
- Return the total diagonal sum

TC: O(n)
SC: O(1)
"""

def diagonalSum(self, mat: list[list[int]]) -> int:

    diagonal_sum = 0
    
    for i in range(len(mat)):
        diagonal_sum += mat[i][i] #primary_diagonal
        diagonal_sum += mat[i][len(mat) - i - 1] # secondary_diagonal


    if len(mat) % 2 != 0:
        middle_index = len(mat) // 2
        diagonal_sum -= mat[middle_index][middle_index]

    return diagonal_sum
    
