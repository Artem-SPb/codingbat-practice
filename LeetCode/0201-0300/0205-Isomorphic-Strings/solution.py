class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Проверяет, являются ли две строки изоморфными.
        Использует две хеш-таблицы для обеспечения строгого маппинга 1-к-1.

        Сложность по времени: O(N)
        Сложность по памяти: O(1) (ограничено размером алфавита)
        """
        # Базовая проверка на случай, если строки разной длины
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        # zip позволяет итерироваться по двум строкам одновременно
        for char_s, char_t in zip(s, t):
            # Проверяем прямую связь (s -> t)
            if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
                return False

            # Проверяем обратную связь (t -> s),
            # чтобы избежать маппинга разных букв в одну
            if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
                return False

            # Фиксируем связь в обоих направлениях
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический успешный случай
    assert solution.isIsomorphic("egg", "add") is True, "Ошибка в тесте 1"

    # Тест 2: Противоречие в прямой связи (o -> a и o -> r)
    assert solution.isIsomorphic("foo", "bar") is False, "Ошибка в тесте 2"

    # Тест 3: Длинные слова без противоречий
    assert solution.isIsomorphic("paper", "title") is True, "Ошибка в тесте 3"

    # Тест 4: Противоречие в обратной связи (b -> d и a -> d)
    assert solution.isIsomorphic("badc", "baba") is False, "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
