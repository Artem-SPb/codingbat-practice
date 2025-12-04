from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Решает задачу "Two Sum" с использованием хэш-таблицы за один проход.

        Сложность по времени: O(n)
        Сложность по памяти: O(n)
        """
        num_map = {}  # Словарь для хранения {значение: индекс}

        # enumerate() позволяет получить и индекс, и значение элемента
        for i, num in enumerate(nums):
            # Вычисляем "дополнение", которое нам нужно найти
            complement = target - num

            # Проверяем, встречали ли мы это дополнение ранее
            if complement in num_map:
                # Если да, то мы нашли решение
                return [num_map[complement], i]

            # Если дополнения нет, добавляем текущее число и его индекс в карту
            # для будущих проверок
            num_map[num] = i
