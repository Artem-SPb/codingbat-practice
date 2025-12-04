// Файл: java/warmup-1/Diff21.java

public class Diff21 {

    /*
     --- Условие ---
     Given an int n, return the absolute difference between n and 21,
     except return double the absolute difference if n is over 21.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Два случая: n > 21 и n <= 21.
     2. Крайние случаи: n = 21 (вернет 0), n = 22 (вернет 2).
        Алгоритм корректен.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: Тернарный оператор в Java:
        `return (n > 21) ? (n - 21) * 2 : 21 - n;`.
        Очень компактно, но if/else может быть чуть нагляднее.
    */

    // --- Решение ---
    public int diff21(int n) {
        if (n > 21) {
            return (n - 21) * 2;
        } else {
            return 21 - n;
        }
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        Diff21 solution = new Diff21();

        System.out.println("Тестирование метода diff21:");
        // Ожидаем: 2
        System.out.println(solution.diff21(19));
        // Ожидаем: 11
        System.out.println(solution.diff21(10));
        // Ожидаем: 8
        System.out.println(solution.diff21(25));
    }
}
