import math 
def inf():
    choise = 0
    I = -1
    i = -1
    K = -1
    N = -1
    while choise != 5:
        choise = int(input("Выберите, что известно: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \n5) Следующий этап\nВаш выбор: "))
        if choise == 1:
            I = int(input('Введите значение в битах: '))
        if choise == 2:
            K = int(input('Введите значение: '))
        if choise == 3:
            i = int(input('Введите значение в битах: '))
        if choise == 4:
            N = int(input('Введите значение в битах: '))
    to_find = int(input("Выберите, что нужно найти: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \n5) Следующий этап\nВаш выбор: "))
    if to_find == 1:
        if i > 0 and K > 0:
            I = K*i 
            print(f"I = {I} бит")
        elif K > 0 and N > 0:
            I = K*math.log2(N)
            print(f"I = {I} бит")
        else:
            print("Недостаточно данных")
    if to_find == 2:
        K =I/i 
        print(f"K = {K} символов")
    if to_find == 3:
        if N > 0:
            i = math.log2(N)
            print(f"i = {i} бит")
        elif K > 0 and I > 0:
            i = I/K
            print(f"i = {i} бит")
        else:
            print("Недостаточно данных")
    if to_find == 4:
        if i > 0:
            N = 2**i
            print(f"N = {N} бит")
        elif I > 0 and K > 0:
            N = 2**(I/K)
            print(f"N = {N} бит")
        else:
            print("Недостаточно данных")
            
def sound():
    print('Здесь будет решение')
prob = int(input("Выберете тип задачи: \n1. задача на информацию \n2. задача на звук \n3. задача на кодирование изображения \nВаш выбор: "))
if prob == 1:
    inf()
elif prob == 2:
    sound()
