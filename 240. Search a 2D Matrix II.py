from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        def helper(start, end):
            if start[0] >= len(matrix) or start[1] >= len(matrix[0]):
                return False

            if start == end:
                return matrix[start[0]][start[1]] == target

            if target < matrix[start[0]][start[1]] or target > matrix[end[0]][end[1]]:
                return False

            m = start[0] + (end[0] - start[0])//2
            n = start[1] + (end[1] - start[1])//2

            a = helper(start, [m, n])
            b = helper([start[0], n+1], [m, end[1]])
            c = helper([m+1, start[1]], [end[0], n])
            d = helper([m+1, n+1], end)

            return a or b or c or d
        return helper([0, 0], [len(matrix)-1, len(matrix[0])-1])


m = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
a = Solution()
print(a.searchMatrix(m, 20))
