"""1) Реализовать функцию,
принимающую два числа (позиционные
аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации
деления на ноль."""

a = True

def division(arg_1, arg_2):

    try:
        arg_1 / arg_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    else:
        global a
        a = False
        return arg_1 / arg_2

while a:
    print(division(int(input("Введите "
                             "первое число: ")), 
                              int(input("Введите "
                              "второе число: "))))