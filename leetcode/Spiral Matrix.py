from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # If the matrix is empty, return an empty list
        if not matrix:
            return []

        ans = []  # This will store the spiral order
        left, right = 0, len(matrix[0])  # Initialize the left and right boundaries
        top, bottom = 0, len(matrix)  # Initialize the top and bottom boundaries

        # Continue the loop until the boundaries overlap
        while left < right and top < bottom:
            # Traverse from left to right on the top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom on the right column
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left

            # Check if the boundaries have overlapped
            if not (left < right and top < bottom):
                break

            # Traverse from right to left on the bottom row
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up

            # Traverse from bottom to top on the left column
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1  # Move the left boundary right

        return ans
