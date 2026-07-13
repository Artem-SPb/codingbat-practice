from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Объединяет перекрывающиеся интервалы.
        Использует предварительную сортировку массива по началу интервалов.

        Сложность по времени: O(N log N)
        Сложность по памяти: O(N)
        """
        # Если интервалов нет или только один, объединять нечего
        if len(intervals) <= 1:
            return intervals

        # Сортируем интервалы по времени начала (x[0])
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # Если список merged пуст или
            # текущий интервал не перекрывается с предыдущим
            # (начало текущего больше конца последнего в merged)
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Интервалы перекрываются. Обновляем конец последнего интервала
                # на максимальное из двух значений концов
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
