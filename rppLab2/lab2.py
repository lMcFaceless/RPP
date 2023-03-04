import numpy as np

arraySize = 5  # Размер матрицы
array = np.random.random((arraySize, arraySize))  # Заполнение матрицы случайными числами
file = open('D:/text.txt', 'w')  # Открытие файла для записи


def main_diagonal():    # Нахождение суммы элементов над главной диагональю
    sumArray = 0
    for i in range(arraySize):
        for j in range(arraySize):
            if j > i:
                sumArray += array[i][j]
                print('Складываемый элемент: ', array[i][j])
    return sumArray


def sec_diagoinal():    # Нахождение произведения элементов над побочной диагональю
    multArray = 1
    for i in range(arraySize):
        for j in range(arraySize):
            if j < arraySize - i - 1:
                multArray *= array[i][j]
                print('Умножаемый элемент: ', array[i][j])
    return multArray


for i in range(arraySize):  # Запись матрицы в файл
    for j in range(arraySize):
        file.write(str(array[i][j]) + ' ')
    file.write('\n')

print(array)
sumArray = main_diagonal()
multArray = sec_diagoinal()
print('Сумма элементов: ', sumArray)
print('Произведение элементов: ', multArray)
file.write('Сумма элементов = ' + str(sumArray) + '\nПроизведение элементов = ' + str(multArray))
file.close()    # Закрытие файла
