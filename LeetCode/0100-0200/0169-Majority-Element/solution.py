from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Находит мажоритарный элемент массива (встречающийся > N/2 раз).
        Использует оптимальный алгоритм голосования Бойера-Мура
        за O(N) времени и O(1) памяти.
        """
        candidate = None
        count = 0

        for num in nums:
            # Если голоса обнулились, выбираем нового кандидата
            if count == 0:
                candidate = num

            # Если встретили сторонника — плюсуем, иначе — минусуем
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Маленький массив
    assert solution.majorityElement([3, 2, 3]) == 3, "Ошибка в тесте 1"

    # Тест 2: Длинный массив с чередованием
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == (
        2, "Ошибка в тесте 2")

    # Тест 3: Массив из одного элемента
    assert solution.majorityElement([42]) == 42, "Ошибка в тесте 3"

    # Тест 4: Элемент большинства стоит в самом конце
    # (проверка сброса кандидата)
    assert solution.majorityElement([1, 2, 3, 3, 3]) == 3, "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
