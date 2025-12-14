// Файл: java/warmup-1/BackAround.java

public class BackAround {

    /*
     --- Условие ---
     Given a string, take the last char and return a new string with the last
     char added at the front and back. The original string will be length 1 or more.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. "Обернуть" строку ее последним символом.
     2. Крайние случаи: Условие гарантирует непустую строку, поэтому
        `str.charAt(str.length() - 1)` всегда будет безопасным вызовом.
     3. Сложность:
        - Временная: O(N).
        - Пространственная: O(N).
     4. Альтернативы: Использование StringBuilder было бы более эффективным для
        очень большого количества конкатенаций, но для этой задачи
        простой оператор `+` является самым читаемым решением.
    */

    // --- Решение ---
    public String backAround(String str) {
        char last = str.charAt(str.length() - 1);
        return last + str + last;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        BackAround solution = new BackAround();

        System.out.println("Тестирование метода backAround:");
        // Ожидаем: tcatt
        System.out.println(solution.backAround("cat"));
        // Ожидаем: oHelloo
        System.out.println(solution.backAround("Hello"));
        // Ожидаем: aaa
        System.out.println(solution.backAround("a"));
    }
}
