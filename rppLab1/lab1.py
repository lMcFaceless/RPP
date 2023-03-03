import random


def quick_sort(list_length):
    if len(list_length) > 1:
        random_number = list_length[random.randint(0, len(list_length) - 1)]  # Выбор случайного значения
        number_smaller = [u for u in list_length if u < random_number]  # Создание списка элементов меньше случайного
        number_equals = [u for u in list_length if u == random_number]  # Создание списка элементов равных случайному
        number_bigger = [u for u in list_length if u > random_number]  # Создание списка элементов больше случайного
        list_length = quick_sort(number_smaller) + number_equals + quick_sort(number_bigger)  # "Пересборка" массива
    return list_length


def input_list():
    numberList = []
    try:
        numberList = [int(el) for el in input().split()]    # Ввод с клавиатуры
    except:
        print('Неправильный формат данных')

    return numberList


numberList = input_list()   # Вызов метода для ввода массива
numberList = quick_sort(numberList)  # Вызов функции
numberListRandom = [random.randint(-10, 10) for _ in range(10)]
numberListRandom = quick_sort(numberListRandom)
print(numberList)  # Вывод отсортированного массива
print(numberListRandom)  # Вывод отсортированного случайного массива
