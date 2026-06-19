from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Находит максимальное количество воды, которое может вместить контейнер.
        Использует паттерн "Два указателя" (сближающиеся с краев).

        Сложность по времени: O(n)
        Сложность по памяти: O(1)
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Ширина контейнера — это разница между индексами
            width = right - left
            # Высота ограничена меньшим из двух бортов
            current_height = min(height[left], height[right])

            # Обновляем максимальную площадь, если текущая больше
            max_area = max(max_area, width * current_height)

            # Всегда сдвигаем указатель, который указывает на меньшую высоту,
            # в надежде найти более высокий борт
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
