from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Группирует анаграммы с использованием хеш-таблицы.
        В качестве ключа используется отсортированная версия строки.

        Сложность по времени: O(N * K log K)
        Сложность по памяти: O(N * K)
        """
        # defaultdict автоматически создает пустой список, если ключа еще нет
        anagram_map = defaultdict(list)

        for s in strs:
            # Сортируем строку. tuple() работает быстрее, чем "".join()
            # Например, 'tea' превратится в ('a', 'e', 't')
            key = tuple(sorted(s))

            # Добавляем оригинальное слово в группу к этому ключу
            anagram_map[key].append(s)

        # Возвращаем только значения словаря (списки сгруппированных слов)
        return list(anagram_map.values())


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Вспомогательная функция для сортировки результата,
    # чтобы порядок групп не влиял на проверку
    # (так как порядок в ответе не важен)
    def normalize(result: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(group) for group in result])

    # Тест 1: Классический случай
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert normalize(solution.groupAnagrams(strs1)) == (
        normalize(expected1), "Ошибка в тесте 1")

    # Тест 2: Пустая строка
    strs2 = [""]
    expected2 = [[""]]
    assert normalize(solution.groupAnagrams(strs2)) == (
        normalize(expected2), "Ошибка в тесте 2")

    # Тест 3: Один символ
    strs3 = ["a"]
    expected3 = [["a"]]
    assert normalize(solution.groupAnagrams(strs3)) == (
        normalize(expected3), "Ошибка в тесте 3")

    print("Все тесты пройдены успешно!")
