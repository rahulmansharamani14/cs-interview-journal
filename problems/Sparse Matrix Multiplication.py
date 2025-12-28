# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

# Example 1:


# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]
# Example 2:

# Input: mat1 = [[0]], mat2 = [[0]]
# Output: [[0]]
 

# Constraints:

# m == mat1.length
# k == mat1[i].length == mat2.length
# n == mat2[i].length
# 1 <= m, n, k <= 100
# -100 <= mat1[i][j], mat2[i][j] <= 100

"""
TC: O(m*n*k)
SC: O(m*n) for creating ans matrix of size m and n
"""

def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:

    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    ans = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            product_sum = 0
            for a in range(k):
                if mat1[i][a] != 0 and mat2[a][j] != 0:
                    product_sum += mat1[i][a] * mat2[a][j]
            ans[i][j] = product_sum
    
    return ans

