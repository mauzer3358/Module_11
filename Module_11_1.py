import requests
from pprint import pprint



##########requests##########работает с http и API запросами
# query = {'text':'Эльбрус'}
# req = requests.get('https://yandex.ru/images/search', params=query)
# print(req.url)
# r = requests.get('https://rosvideo.site')
# r.content
# r.text
# print(r.text)
# print(r.headers)

##########pandas##########работает с файлами CSV,Excel, с табличными данными
import pandas as pd
import numpy as np

# d = {'feature1': [4,3,2,1,0], 'feature2': ['x', 'z', 'y', 'x', 'z'], 'feature3': [2,3,4,1,0]}
# df1 = pd.DataFrame(d)
# print(df1)
# data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]}
# df2 = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4'])
# print(df2)
#
# print('Вывести 3 строки:')
# print(df1.head(3))
# print('метод инфо:')
# df2.info()
# print('поиск элемента:')
# print(df1.iloc[1,1])
# print('замена элемента:')
# print(df1.replace(4,7))



##########numpy########## работает с большими многомерными массивами и матрицами
a1=np.array([1,2,3,6], dtype='float32') #целые числа переведены в числа с плавающей точкой
a2 = np.array([[1, 2, 3], [4, 5, 6]])
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a1)
print('число измерений:',a1.ndim, 'размер, форма массива: ',a1.shape, 'кол-во эл-тов массива: ', a1.size)
print(a2)
print('число измерений:',a2.ndim, 'размер, форма массива: ',a2.shape, 'кол-во эл-тов массива: ', a2.size)
print(a3)
print('число измерений:',a3.ndim, 'размер, форма массива: ',a3.shape, 'кол-во эл-тов массива: ', a3.size)
print('достать элемент', a3[1,1,0], a2[1,2])
print('достать строку', a3[0,1, :])
print('достать столбец', a2[:, 0])
print('замена элемента:')
a2[1,0] = 9
print(a2)

#########matplotlib########### создает графики на основе данных
import matplotlib.pyplot as plt


x = [10, 20, 30, 40, 50]
y = [15, 27, 34, 13, 29]

# plt.plot(x,y)
# plt.xlabel('Значения Х')
# plt.ylabel('Значения Y')
# plt.title('Такой вот график')
# plt.show()

plt.scatter(x, y)
plt.show()

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [20, 44, 33, -2, 7]

plt.bar(x, y, label='Величина прибыли') #Столбчатая диаграмма Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()

vals = [24, 17, 53, 21, 35]
model = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=model, autopct='%1.1f%%')   #круговая по параметрам с процентами + кол-во знаков после запятой
plt.title("Распределение марок автомобилей на дороге")
plt.show()



#########Pillow########### работа с изображениями

from PIL import Image

filename = './materials-python-pillow/buildings.jpg'
with Image.open(filename) as img:
    img.load()
type(img)

isinstance(img, Image.Image)

img.show()
print('формат',img.format)
print('размер', img.size)
print('режим', img.mode)

cropped_img = img.crop((300, 150, 700, 1000)) #обрезка
print(cropped_img.size)
cropped_img.show()

low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4)) #изменение размера
low_res_img.show()









