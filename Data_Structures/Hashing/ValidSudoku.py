# Valid Sudoku

# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# The input corresponding to the above configuration :
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.

# Note:

# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
    # @param A : tuple of strings (each representing a row of the Sudoku)
    # @return an integer (1 for valid Sudoku, 0 for invalid Sudoku)
    def isValidSudoku(self, A):
        # Step 1: Convert the tuple input into a 2D matrix representation (list of lists)
        sudoku = []  # Initialize an empty list to store the Sudoku matrix
        for i in A:
            # Strip any unnecessary whitespace and convert each string row to a list of characters
            temp = list(i.strip())  
            sudoku.append(temp)  # Append the converted row to the Sudoku matrix
        
        # Step 2: Check for duplicates in each row
        for i in sudoku:
            row_hash = {}  # Initialize an empty dictionary to track seen characters in the current row
            for char in i:
                # If the character is already in the row and is not a '.', it is a duplicate
                if char in row_hash and char != '.':
                    return 0  # Invalid Sudoku, return 0
                else:
                    # Add the character to the hash map (ignore '.' as it represents an empty cell)
                    row_hash[char] = 1
        
        # Step 3: Check for duplicates in each column
        for i in range(9):  # Loop through each column index from 0 to 8
            col_hash = {}  # Initialize a hash map to track seen characters in the current column
            for j in range(9):  # Loop through each row for the given column index
                char = sudoku[j][i]  # Access the element in the current column (i) and row (j)
                # If the character is already in the column and is not a '.', it is a duplicate
                if char in col_hash and char != '.':
                    return 0  # Invalid Sudoku, return 0
                else:
                    # Add the character to the hash map (ignore '.' as it represents an empty cell)
                    col_hash[char] = 1
        
        # Step 4: Check for duplicates in each 3x3 sub-grid
        # Each sub-grid starts at index (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), and (6,6)
        for box_row in range(0, 9, 3):  # Iterate through starting rows of each 3x3 sub-grid
            for box_col in range(0, 9, 3):  # Iterate through starting columns of each 3x3 sub-grid
                box_hash = {}  # Initialize a hash map to track seen characters in the current sub-grid
                # Traverse through the 3x3 sub-grid starting at (box_row, box_col)
                for i in range(3):  # Iterate over the 3 rows of the current 3x3 sub-grid
                    for j in range(3):  # Iterate over the 3 columns of the current 3x3 sub-grid
                        # Access the element in the sub-grid
                        num = sudoku[box_row + i][box_col + j]
                        # If the number is already in the sub-grid and is not a '.', it is a duplicate
                        if num in box_hash and num != '.':
                            return 0  # Invalid Sudoku, return 0
                        else:
                            # Add the number to the hash map (ignore '.' as it represents an empty cell)
                            box_hash[num] = 1

        # Step 5: If no duplicates were found, return 1 (the Sudoku is valid)
        return 1
s = Solution()
sudoku_board = (
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79"
)
print(s.isValidSudoku(sudoku_board))  # Output: 1 for valid Sudoku, 0 otherwise
