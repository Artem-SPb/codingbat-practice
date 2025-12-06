// Файл: java/warmup-1/Makes10.java

public class Makes10 {

    /*
     --- Условие ---
     Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Проверяем три условия через "ИЛИ":
        a == 10, b == 10, a + b == 10.
     2. Крайние случаи: Отрицательные числа, нули. Алгоритм корректен.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: Нет. Прямое логическое выражение - лучший способ.
    */

    // --- Решение ---
    public boolean makes10(int a, int b) {
        return (a == 10 || b == 10 || a + b == 10);
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        Makes10 solution = new Makes10();

        System.out.println("Тестирование метода makes10:");
        // Ожидаем: true
        System.out.println(solution.makes10(9, 10));
        // Ожидаем: false
        System.out.println(solution.makes10(9, 9));
        // Ожидаем: true
        System.out.println(solution.makes10(1, 9));
    }
}
