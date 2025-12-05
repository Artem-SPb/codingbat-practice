// Файл: java/warmup-1/ParrotTrouble.java

public class ParrotTrouble {

    /*
     --- Условие ---
     We have a loud talking parrot. The "hour" parameter is the current hour
     time in the range 0..23. We are in trouble if the parrot is talking and
     the hour is before 7 or after 20. Return True if we are in trouble.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Проблема = (попугай говорит) И
        (время раннее ИЛИ позднее).
     2. Крайние случаи: hour = 6, 7, 20, 21. Алгоритм корректен.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: Использование if/else, но оно избыточно.
    */

    // --- Решение ---
    public boolean parrotTrouble(boolean talking, int hour) {
        return (talking && (hour < 7 || hour > 20));
    }


    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        ParrotTrouble solution = new ParrotTrouble();

        System.out.println("Тестирование метода parrotTrouble:");
        // Ожидаем: true
        System.out.println(solution.parrotTrouble(true, 6));
        // Ожидаем: false
        System.out.println(solution.parrotTrouble(true, 7));
        // Ожидаем: false
        System.out.println(solution.parrotTrouble(false, 6));
    }
}
