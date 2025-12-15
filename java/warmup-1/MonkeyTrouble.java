// Файл: java/warmup-1/MonkeyTrouble.java

public class MonkeyTrouble {

    /*
     --- Условие ---
     We have two monkeys, a and b, and the parameters a_smile and b_smile
     indicate if each is smiling. We are in trouble if they are both smiling
     or if neither of them is smiling. Return True if we are in trouble.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Проблема, если состояния двух
        обезьян совпадают.
     2. Крайние случаи: Отсутствуют.
     3. Сложность:
        - Временная: O(1) - одна операция сравнения.
        - Пространственная: O(1) - дополнительная память не используется.
     4. Альтернативы: Как и в Python, можно было бы использовать
        (aSmile && bSmile) || (!aSmile && !bSmile), но прямое сравнение
        через '==' является лучшей практикой.
    */

    // --- Решение ---
    public boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
        return aSmile == bSmile;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        MonkeyTrouble solution = new MonkeyTrouble();

        System.out.println("Тестирование метода monkeyTrouble:");
        // Ожидаем: true
        System.out.println(solution.monkeyTrouble(true, true));
        // Ожидаем: true
        System.out.println(solution.monkeyTrouble(false, false));
        // Ожидаем: false
        System.out.println(solution.monkeyTrouble(true, false));
    }
}
