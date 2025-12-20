import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Находит k самых часто встречающихся элементов.

        Сложность по времени: O(N log k)
        Сложность по памяти: O(N) в худшем случае для словаря частот.
        """
        # Этап 1: Подсчет частот всех элементов в массиве.
        # Counter - это удобная разновидность словаря для подсчета.
        # O(N) по времени.
        if not nums:
            return []

        freq_map = Counter(nums)

        # Этап 2: Использование min-heap для нахождения k элементов
        # с наибольшей частотой.
        # O(M log k) по времени, где M - количество уникальных элементов.
        min_heap = []

        # Итерируемся по парам (элемент, частота)
        for num, freq in freq_map.items():
            # В кучу кладем кортеж (частота, элемент).
            # Куча будет сортироваться по первому элементу кортежа,
            # т.е. по частоте.
            heapq.heappush(min_heap, (freq, num))
            # Поддерживаем размер кучи не более k.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Этап 3: Извлекаем результат.
        # В куче остались k элементов с самыми высокими частотами.
        result = []
        for freq, num in min_heap:
            result.append(num)

        return result
