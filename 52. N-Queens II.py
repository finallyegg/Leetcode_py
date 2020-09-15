class Solution:
    def totalNQueens(self, n: int) -> int:

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

        def remove_queen(row, col):
            plus[row+col] = 0
            minus[row-col] = 0
            col_c[col] = 0

        def backtrace(row=0, count=0):
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrace(row + 1,  count)
                    remove_queen(row, col)
            return count

        return backtrace()
