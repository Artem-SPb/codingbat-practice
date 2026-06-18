from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Перемещает все нули в конец массива,
        сохраняя порядок остальных элементов.
        Модифицирует массив in-place, ничего не возвращает.

        Сложность по времени: O(n)
        Сложность по памяти: O(1)
        """
        # Указатель на позицию,
        # куда мы будем вставлять следующий ненулевой элемент
        insert_pos = 0

        for i in range(len(nums)):
            # Если текущий элемент не равен нулю
            if nums[i] != 0:
                # Меняем местами текущий элемент
                # с элементом на позиции insert_pos
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                # Сдвигаем позицию для следующей вставки
                insert_pos += 1
