// Файл: java/warmup-2/Last2.java

public class Last2 {

    /*
     --- Условие ---
     Given a string, return the count of the number of times that a substring
     length 2 appears in the string and also as the last 2 chars of the string.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Берем последние 2 символа
        и ищем их в остальной части строки с помощью цикла.
     2. Крайние случаи: Строка длиной < 2. Обрабатывается в начале.
     3. Сложность:
        - Временная: O(N).
        - Пространственная: O(1).
     4. Альтернативы: Нет, цикл - это стандартный подход. Важно помнить
        про использование `.equals()` для сравнения строк, а не `==`.
    */

    // --- Решение ---
    public int last2(String str) {
        if (str.length() < 2) {
            return 0;
        }

        String end = str.substring(str.length() - 2);
        int count = 0;

        // Цикл до предпоследней возможной пары
        for (int i = 0; i < str.length() - 2; i++) {
            String sub = str.substring(i, i + 2);
            if (sub.equals(end)) {
                count++;
            }
        }

        return count;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        Last2 solution = new Last2();

        System.out.println("Тестирование метода last2:");
        // Ожидаем: 1
        System.out.println(solution.last2("hixxhi"));
        // Ожидаем: 1
        System.out.println(solution.last2("xaxxaxaxx"));
        // Ожидаем: 2
        System.out.println(solution.last2("axxxaaxx"));
    }
}
