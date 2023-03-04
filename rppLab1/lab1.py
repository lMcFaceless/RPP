import random


def bubble_sort(sort_list):
    for i in range(len(sort_list) - 1):
        for j in range(len(sort_list) - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]  # Элементы меняются местами
    return numberList


def st_sort(st_sort_list):  # Сортировка массива с использованием стандартной функции
    list.sort(st_sort_list)
    return st_sort_list


def input_list():
    inputList = []
    try:
        inputList = [int(el) for el in input().split()]  # Ввод с клавиатуры
    except:
        print('Неправильный формат данных')

    return inputList


numberList = input_list()  # Вызов метода для ввода массива
numberList = bubble_sort(numberList)  # Вызов метода для сортировки массива
numberListRandom = [random.randint(-10, 10) for _ in range(10)]  # Заполнение массива случайными числами
numberListRandom = st_sort(numberListRandom)  # Вызов метода для сортировки случайного массива
print('Отсортированный массив: ', numberList)  # Вывод отсортированного массива
print('Отсортированный случайный массив: ', numberListRandom)  # Вывод отсортированного случайного массива
