import os

import pandas
import pandas as pd

data = pd.read_csv("data.csv")
print(data.head())

oldpath = os.getcwd()
files = os.listdir()
print("Количество файлов в папке: ", len(files))

dataDict = data.to_dict()
print(dataDict)

names = dataDict.get("name")
names = dict(sorted(names.items(), key=lambda item: item[1]))
print("Сортировка по имени: ", names)

quantities = dataDict.get("quantity")
quantities = dict(sorted(quantities.items(), key=lambda item: item[1]))

print("Сортировка по количеству, больше 100: ")
for i in quantities.items():
    if i[1] > 100:
        print(i)

newRow = [len(quantities.items()) + 1, "Borsch", 100, "2021-07-25 16:17:45.04", "2021-07-25 16:18:00.00", 20]
data.loc[len(data)] = newRow
print(data)
data.to_csv("data.csv", index=False)
