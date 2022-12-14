"""4)4) Программа принимает
действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение
числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y).
При решении задания необходимо
обойтись без встроенной функции
возведения числа в степень.
Подсказка: попробуйте решить задачу
двумя способами. Первый — возведение
в степень с помощью оператора
возведения в степень. Второй — более
сложная реализация без оператора
возведения в степень,
предусматривающая использование
цикла."""

"""1 способ"""
def my_func(x, y):
    result = x ** y
    return print(result)

my_func(float(input("Введите "
                "действительное положительное"
                " число: ")), int(input("Введите "
                "целое отрицательное число: ")))

"""2 способ"""
def my_func_1(x, y):
    i = 1
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    return (print(1 / result))

my_func_1(float(input("Введите "
                "действительное положительное"
                " число: ")), int(input("Введите "
                "целое отрицательное число: ")))