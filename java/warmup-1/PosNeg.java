// Файл: java/warmup-1/PosNeg.java

public class PosNeg {

    /*
     --- Условие ---
     Given 2 int values, a and b, and a boolean parameter "negative".
     If negative is true, then return true only if both a and b are negative.
     If negative is false, then return true if one is negative and one is positive.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python, разветвляется по `negative`.
     2. Крайние случаи: 0 обрабатывается корректно.
     3. Сложность: O(1) по времени и пространству.
     4. Альтернативы: Для `negative == false`, можно было бы написать
        `(a < 0 && b > 0) || (a > 0 && b < 0)`, но `a * b < 0` короче.
    */

    // --- Решение ---
    public boolean posNeg(int a, int b, boolean negative) {
        if (negative) {
            return (a < 0 && b < 0);
        } else {
            return (a * b < 0);
        }
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        PosNeg solution = new PosNeg();

        System.out.println("Тестирование метода posNeg:");
        // Ожидаем: true
        System.out.println(solution.posNeg(1, -1, false));
        // Ожидаем: true
        System.out.println(solution.posNeg(-4, -5, true));
        // Ожидаем: false
        System.out.println(solution.posNeg(-4, -5, false));
    }
}
