"""Напишите программу, которая найдёт
произведение пар чисел списка. Парой
считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

def couple_sum():
    result = 0
    user_list = input("Введите числа через "
                      "пробел:").split()
    for i in range(0, (len(user_list) // 2)):
        result = \
            int(user_list[i]) * int(user_list[-(i + 1)])
        print(result)

couple_sum()