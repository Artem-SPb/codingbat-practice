from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Сортирует массив из 0, 1 и 2 на месте (in-place) за один проход.
        Использует алгоритм Голландского национального флага
        (Dutch National Flag) с тремя указателями.

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        left = 0
        curr = 0
        right = len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                # Нашли 0 — кидаем его в левую часть
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                # Нашли 2 — кидаем её в правую часть
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                # curr НЕ сдвигаем, так как элемент,
                # пришедший с позиции right, еще не проверен
            else:
                # Нашли 1 — оставляем в центре, просто идем дальше
                curr += 1


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Регулярный массив из примера
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    assert nums1 == [0, 0, 1, 1, 2, 2], f"Ошибка в тесте 1: {nums1}"

    # Тест 2: Короткий массив
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    assert nums2 == [0, 1, 2], f"Ошибка в тесте 2: {nums2}"

    # Тест 3: Уже отсортированный массив
    nums3 = [0, 1, 2]
    solution.sortColors(nums3)
    assert nums3 == [0, 1, 2], f"Ошибка в тесте 3: {nums3}"

    # Тест 4: Массив из одинаковых элементов
    nums4 = [1, 1, 1]
    solution.sortColors(nums4)
    assert nums4 == [1, 1, 1], f"Ошибка в тесте 4: {nums4}"

    # Тест 5: Массив без единиц
    nums5 = [2, 0, 2, 0]
    solution.sortColors(nums5)
    assert nums5 == [0, 0, 2, 2], f"Ошибка в тесте 5: {nums5}"

    print("Все тесты пройдены успешно!")
