class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def find_subBox(row, col):
            return row // 3 * 3 + col // 3

        def is_valid(row, col, value):
            return not (value in row_d[row] or
                        value in col_d[col] or
                        value in subbox[find_subBox(row, col)])

        def place(row, col, value):
            row_d[row].add(value)
            col_d[col].add(value)
            subbox[find_subBox(row, col)].add(value)
            board[row][col] = str(value)

        def remove(row, col, value):
            row_d[row].remove(value)
            col_d[col].remove(value)
            subbox[find_subBox(row, col)].remove(value)
            board[row][col] = '.'

        def find_next(row, col):
            if row == 8 and col == 8:
                nonlocal solved
                solved = True
            else:
                if col == 8:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col+1)

        def backtrack(row=0, col=0):

            if board[row][col] == '.':
                for i in range(1, 10):
                    if is_valid(row, col, i):
                        place(row, col, i)
                        find_next(row, col)
                        nonlocal solved
                        if not solved:
                            remove(row, col, i)
            else:
                find_next(row, col)

        row_d = {}
        col_d = {}
        subbox = {}
        solved = False

        for i in range(9):
            row_d[i] = set()
            col_d[i] = set()
            subbox[i] = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    row_d[i].add(int(board[i][j]))
                    col_d[j].add(int(board[i][j]))
                    subbox[find_subBox(i, j)].add(int(board[i][j]))

        backtrack()
