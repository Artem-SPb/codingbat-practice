// Файл: java/warmup-2/ArrayCount9.java

public class ArrayCount9 {

    // --- Условие ---
    // Given an array of ints, return the number of 9's in the array.

    // --- Мой анализ ---
    // 1. Понимание: Нужно итеративно пройти по массиву и посчитать девятки.
    // 2. Крайние случаи: Пустой массив (цикл не выполнится, вернется 0).
    // 3. Сложность:
    //    - Временная: O(N).
    //    - Пространственная: O(1).
    // 4. Альтернативы: Использование Java Streams (более современный подход),
    //    но для базовых задач цикл for является стандартным решением.

    // --- Решение ---
    public int arrayCount9(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (num == 9) {
                count++;
            }
        }
        return count;
    }
}
