class Solution:
    def matSearch(self, mat, x):
        m = len(mat)
        n = len(mat[0])

        row = 0
        col = n - 1

        while row < m and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1
            else:
                row += 1

        return False