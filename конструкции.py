import random
from turtle import *
while True:
    q = random.randint(1, 50)
    q1 = random.randint(1, 50)
    print(f"{q} + {q1} = ")
    a = int(input())
    if a != q + q1:         # вечный цикл с выходом по break
        break

for x in range(2):
   for y in range(2): # двойной пребор из диапазона 2 значений (0,1) в дмумерном массиве или подбор двух параметров
        print(f'x = {x}, y = {y}')         # выход из цикла

def stroki():
    i = str(34101010)
    num=(bin(i)[2:])         # перевод в 2 и срез мусора
    print(num.count('1'))           # количество входов символа в списке/строке
    print(num.index('6'))          # индекс эелмента в списке/строке
    print(num.append('56'))            # добавить значение n
    print(num.sort(reverse=True))   # сортировать список по убыванию
    chislo='10'+num[2:]+'0'  # склейка
    print(int(chislo,2))
    data=[]   
    for w in range(1, 10):
        w = random.randint(1, 50)
        data.append(w)               
    spisok=set(x for x in data if x >= 10)  # использовани генератора для экономии строк
    print(spisok)
    a = 'GJVJUBNT'
    b = a.split() 
    print(b) 


def f(n):
   return 2*f(n-2)      # рекурсия
print(f(26))

def tuurtl():
    left(90)     # поворот налево 90гр
    forward(300) # вперед на 300 единиц
    right(120)   # поворот направо 120гр
    pu()         # поднять перо
    goto(x*30,y*30)  # переходить по точкам
    dot(5)           # нарисовать точку          
    done()           # запустить рисование