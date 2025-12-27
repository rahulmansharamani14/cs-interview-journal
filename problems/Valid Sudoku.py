# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


"""
Approach: Using Set
- For row check, use a set (row_set)
- For column check, use a set (column_set)
- For sub-boxes check, use a hashmap with key: (r//3, c//3) and value as a set (sub_boxe_set)

TC: O(n * n) for traversing through the entire grid
SC: O(n * n) for extra space using hashmap and set (in worst case)
"""

from collections import defaultdict

def isValidSudoku(self, board: list[list[str]]) -> bool:

    row_set = defaultdict(set)
    column_set = defaultdict(set)
    sub_boxes = defaultdict(set) #key: (r//3, c//3), val: set

    n = len(board)

    for r in range(n):
        for c in range(n):
            if board[r][c] == ".":
                continue

            if (board[r][c] in row_set[r]) or (board[r][c] in column_set[c]):
                return False
            
            if board[r][c] in sub_boxes[(r//3, c//3)]:
                return False
            
            row_set[r].add(board[r][c])
            column_set[c].add(board[r][c])
            sub_boxes[(r//3,c//3)].add(board[r][c])

    return True

