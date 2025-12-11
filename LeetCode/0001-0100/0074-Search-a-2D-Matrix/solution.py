from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Ищет target в отсортированной 2D матрице, рассматривая ее как
        одномерный массив и применяя бинарный поиск.

        Сложность по времени: O(log(m*n))
        Сложность по памяти: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        # Представляем матрицу как виртуальный одномерный массив
        # от 0 до (rows * cols - 1)
        left, right = 0, rows * cols - 1

        while left <= right:
            # mid - это индекс в нашем виртуальном 1D массиве
            mid = (left + right) // 2

            # Преобразуем 1D индекс mid обратно в 2D координаты (row, col)
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
