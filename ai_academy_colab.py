# -*- coding: utf-8 -*-
"""AI_Academy_Colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ai-academy318/aiacademy/blob/master/AI_Academy_Colab.ipynb
"""

### 下記の入力フィールドにプログラムを打ち込み、左の実行ボタンを押す事で書いたコードを実行できます。　###

years_list = [2017,2018,2019,2020,2021]
print(years_list[3])
print(years_list[4])

myFavorite_num = [3,7,55]
myFavorite_num.append(13)
print(myFavorite_num)

profile = {'hamada': 52, 'matumoto': 52, 'shigeru': 13}
print(profile)

age = 20
if age >= 20:
  print('成人です')
else:
  print('子供です')

result = [x**2 for x in range(1,11)]
print(result)

countDown = [3,2,1,'Go!']
for i in countDown:
  print(i)

counter = []
for i in range(1, 101):
    if i % 2 == 0:
        counter.append(i)

print(counter)