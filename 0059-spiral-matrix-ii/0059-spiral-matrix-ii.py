class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, down = 0, n - 1
        left, right = 0, n - 1
        curr_element = 1

        while curr_element <= n * n:
            for c in range(left, right + 1):
                matrix[top][c] = curr_element
                curr_element += 1
            top += 1

            for r in range(top, down + 1):
                matrix[r][right] = curr_element
                curr_element += 1
            right -= 1

            c = right
            while c >= left and curr_element <= n * n:
                matrix[down][c] = curr_element
                curr_element += 1
                c -= 1
            down -= 1

            r = down
            while r >= top and curr_element <= n * n:
                matrix[r][left] = curr_element
                curr_element += 1
                r -= 1
            left += 1

        return matrix