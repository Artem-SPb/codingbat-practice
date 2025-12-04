from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Проверяет, содержит ли массив дубликаты, с использованием хэш-сета.

        Сложность по времени: O(n)
        Сложность по памяти: O(n)
        """
        hashset = set()

        for num in nums:
            # Если число уже есть в сете, значит мы нашли дубликат
            if num in hashset:
                return True
            # Если числа нет, добавляем его в сет для отслеживания
            hashset.add(num)

        # Если цикл завершился, дубликатов не найдено
        return False
