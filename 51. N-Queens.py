class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        plus = {}
        minus = {}
        col_c = {}
        for i in range(n):
            col_c[i] = 0
        for i in range(2*n - 1):
            plus[i] = 0
            minus[i-(n-1)] = 0

        def is_safe(row, col):
            return not (plus[row+col] or minus[row-col] or col_c[col])

        def place_queen(row, col):
            plus[row+col] = 1
            minus[row-col] = 1
            col_c[col] = 1
            grid[row][col] = 'Q'

        def remove_queen(row, col):
            plus[row+col] = 0
            minus[row-col] = 0
            col_c[col] = 0
            grid[row][col] = '.'

        def backtrace(row=0):
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        solution = []
                        for line in grid:
                            str1 = "".join(line)
                            solution.append(str1)
                        result.append(solution)
                    else:
                        backtrace(row + 1)
                    remove_queen(row, col)

        backtrace()
        return result
