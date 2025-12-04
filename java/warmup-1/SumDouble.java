// Файл: java/warmup-1/SumDouble.java

public class SumDouble {

    /*
     --- Условие ---
     Given two int values, a and b, return their sum. Unless the values are the
     same, then return double their sum.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Если числа равны, вернуть
        удвоенную сумму, иначе - обычную.
     2. Крайние случаи: 0, отрицательные числа. Алгоритм корректен.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: Можно использовать тернарный оператор, который в Java
        очень популярен: `return (a == b) ? (a + b) * 2 : a + b;`.
    */

    // --- Решение ---
    public int sumDouble(int a, int b) {
        int sum = a + b;
        if (a == b) {
            sum = sum * 2;
        }
        return sum;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        SumDouble solution = new SumDouble();

        System.out.println("Тестирование метода sumDouble:");
        // Ожидаем: 3
        System.out.println(solution.sumDouble(1, 2));
        // Ожидаем: 12
        System.out.println(solution.sumDouble(3, 3));
        // Ожидаем: 8
        System.out.println(solution.sumDouble(2, 2));
    }
}
