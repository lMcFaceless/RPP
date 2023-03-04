import random


def bubble_sort(numberList):
    for i in range(len(numberList) - 1):
        for j in range(len(numberList) - i - 1):
            if numberList[j] > numberList[j + 1]:
                numberList[j], numberList[j + 1] = numberList[j + 1], numberList[j]  # Элементы меняются местами
    return numberList


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
numberListRandom = bubble_sort(numberListRandom)  # Вызов метода для сортировки случайного массива
print('Отсортированный массив: ', numberList)  # Вывод отсортированного массива
print('Отсортированный случайный массив: ', numberListRandom)  # Вывод отсортированного случайного массива
