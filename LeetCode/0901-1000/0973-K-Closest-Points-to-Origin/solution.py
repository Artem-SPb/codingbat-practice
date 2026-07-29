import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Находит K ближайших точек к началу координат за O(N).
        Использует алгоритм Быстрого выбора (Quick Select),
        основанный на механике Быстрой сортировки (Quick Sort).
        """
        def dist(i: int) -> int:
            # Вычисляем квадрат расстояния (x^2 + y^2) для точки по индексу i
            return points[i][0]**2 + points[i][1]**2

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_dist = dist(pivot_index)

            # 1. Прячем опорный элемент (pivot) в конец массива
            points[pivot_index], points[right] = (
                points[right], points[pivot_index])

            store_index = left
            # 2. Проходим по массиву и кидаем все элементы,
            # которые меньше pivot, влево
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[store_index], points[i] = (
                        points[i], points[store_index])
                    store_index += 1

            # 3. Возвращаем опорный элемент на его финальное законное место
            points[right], points[store_index] = (
                points[store_index], points[right])

            # Теперь всё, что слева от store_index,
            # строго меньше опорного элемента
            return store_index

        def quick_select(left: int, right: int, K: int) -> None:
            if left >= right:
                return

            # Берем случайный элемент в качестве pivot
            # (спасает от O(N^2) в худшем случае)
            pivot_index = random.randint(left, right)

            # Ставим pivot на место и получаем его итоговый индекс
            pivot_index = partition(left, right, pivot_index)

            # В отличие от Quick Sort,
            # мы идем только в ОДНУ нужную нам половину!
            if pivot_index == K:
                # Массив разделен идеально,
                # слева от K ровно K мельчайших элементов
                return
            elif pivot_index < K:
                # Наш pivot оказался левее искомой границы.
                # Идем искать в правую часть.
                quick_select(pivot_index + 1, right, K)
            else:
                # Наш pivot оказался правее искомой границы.
                # Идем искать в левую часть.
                quick_select(left, pivot_index - 1, K)

        # Запускаем алгоритм
        quick_select(0, len(points) - 1, k)

        # Возвращаем первые K элементов
        return points[:k]


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Вспомогательная функция для сравнения
    # (т.к. порядок точек в ответе не важен)
    def normalize(points_list):
        return sorted(points_list)

    # Тест 1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    expected1 = [[-2, 2]]
    assert normalize(solution.kClosest(points1, k1)) == (
        normalize(expected1), "Ошибка в тесте 1")

    # Тест 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    expected2 = [[3, 3], [-2, 4]]
    assert normalize(solution.kClosest(points2, k2)) == (
        normalize(expected2), "Ошибка в тесте 2")

    # Тест 3: K равно длине массива
    points3 = [[1, 1], [2, 2], [3, 3]]
    k3 = 3
    expected3 = [[1, 1], [2, 2], [3, 3]]
    assert normalize(solution.kClosest(points3, k3)) == (
        normalize(expected3), "Ошибка в тесте 3")

    print("Все тесты пройдены успешно!")
