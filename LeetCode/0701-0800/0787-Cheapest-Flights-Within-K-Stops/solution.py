from typing import List


class Solution:
    def findCheapestPrice(
            self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        Находит минимальную стоимость перелета
        с ограничением по количеству пересадок.
        Использует адаптированный алгоритм Беллмана-Форда (Bellman-Ford).
        """
        # Изначально цены до всех городов равны бесконечности
        prices = [float('inf')] * n
        prices[src] = 0

        # k пересадок = k + 1 перелет (шаг)
        for _ in range(k + 1):
            # Создаем временную копию,
            # чтобы избежать "цепной реакции" обновлений в пределах одного шага
            tmp_prices = prices.copy()

            for u, v, price in flights:
                # Если мы вообще можем вылететь из города u на данном этапе
                if prices[u] != float('inf'):
                    # Обновляем цену до города v во временном массиве
                    if prices[u] + price < tmp_prices[v]:
                        tmp_prices[v] = prices[u] + price

            # Фиксируем цены для следующего шага
            prices = tmp_prices

        # Если цена до пункта назначения осталась бесконечной, маршрута нет
        return prices[dst] if prices[dst] != float('inf') else -1


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Более дешевый путь блокируется лимитом пересадок (k=1)
    flights1 = [
        [0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert solution.findCheapestPrice(4, flights1, 0, 3, 1) == (
        700, "Ошибка в тесте 1")

    # Тест 2: Тот же граф, но разрешено 2 пересадки (путь через 2 открывается)
    assert solution.findCheapestPrice(4, flights1, 0, 3, 2) == (
        400, "Ошибка в тесте 2")

    # Тест 3: Невозможно добраться
    flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert solution.findCheapestPrice(3, flights3, 0, 2, 0) == (
        500, "Ошибка в тесте 3")

    print("Все тесты пройдены успешно!")
