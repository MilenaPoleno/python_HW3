"""3) Реализовать функцию my_func(),
которая принимает три позиционных
аргумента, и возвращает сумму
наибольших двух аргументов."""

def my_func(arg_1, arg_2, arg_3):
    my_sum = arg_1 + arg_2 + arg_3
    min_arg = min([arg_1, arg_2, arg_3])
    result = my_sum - min_arg
    return  print(result)
my_func(int(input("Введите первое "
                "число: ")), int(input("Введите "
                "второе число: ")), int(input(
                "Введите третье число: ")))