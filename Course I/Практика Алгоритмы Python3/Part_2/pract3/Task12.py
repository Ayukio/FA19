def input_numbers():
    """Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом
    0. Выведите первое, третье, пятое и т.д. из введенных чисел. Завершающий ноль выводить не
    надо.
    В этой задаче нельзя использовать глобальные переменные и передавать какие-либо параметры
    в рекурсивную функцию. Функция получает данные, считывая их с клавиатуры. Функция не
    возвращает значение, а сразу же выводит результат на экран. Основная программа должна
    состоять только из вызова этой функции. (два базовых случая)"""
    n_one = input_N()
    if n_one > 0:
        n_two = input_N()
        print(n_one)
        if n_two > 0:
            input_numbers()
        else:
            print("Конец")
    else:
        print("Конец")
def input_N():
    #Ввод числа N
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

input_numbers()