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
    to_find = int(input("Выберите, что нужно найти: \n1) I - информационный объём текста \n2) К - количество символов в тексте \n3) i - информационный вес одного символа \n4) N - мощность алфавита \nВаш выбор: "))
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
    choise = 0
    H = -1
    I = -1
    t = -1
    b = -1
    while choise != 5:
        choise = int(input("Выберите, что известно: \n1) H - частота дискретизации \n2) I - объём звуковой информации \n3) t - время записи звука \n4) b - разрядность квантования \n5) Следующий этап\nВаш выбор: "))
        if choise == 1:
            H = int(input('Введите значение в Гц: '))
        if choise == 2:
            I = int(input('Введите значение в байтах: '))
        if choise == 3:
            t = int(input('Введите значение в секундах: '))
        if choise == 4:
            b = int(input('Введите значение в байтах: '))
    to_find = int(input("Выберите, что нужно найти: \n1) H - частота дискретизации \n2) I - объём звуковой информации \n3) t - время записи звука \n4) b - разрядность квантования \nВаш выбор: "))
    if to_find == 1:
        H = I/(b*t)
        print(f"H = {H} Гц")
    if to_find == 2:
        I = H*t*b
        print(f"I = {I} байт")
    if to_find == 3:
        t = I/(H*b)
        print(f"t = {t} секунд")
    if to_find == 4:
       b = I/(H*t)
       print(f"b = {b} байт")

def image():
    choise = 0
    b = -1
    I = -1
    x = -1
    y = -1
    K = -1
    while choise != 6:
        choise = int(input("Выберите, что известно: \n1) b - битовая глубина кодирования \n2) I - объём информации \n3) х - количество пикселей по горизонтали \n4) у - количество пикселей по вертикали \n5) К - количество оттенков \n6)Следующий этап \nВаш выбор: "))
        if choise == 1:
            b = int(input('Введите значение в битах: '))
        if choise == 2:
            I = int(input('Введите значение в битах: '))
        if choise == 3:
            x = int(input('Введите значение: '))
        if choise == 4:
            y = int(input('Введите значение: '))
        if choise == 5:
            K = int(input("Введите значение: "))
    to_find = int(input("Выберите, что нужно найти: \n1) b - битовая глубина кодирования \n2) I - объём информации  \n3) К - количество оттенков \nВаш выбор: "))
    if to_find == 1:
        if K > 0:
            b = math.log2(K)
        elif I > 0:
            b = I/(x*y)
        print(f"b = {b} бит")
    if to_find == 2:
        I = y*x*b
        print(f"I = {I} бит")
    if to_find == 3:
        K = 2**b
        print(f"K = {K} ")

prob = int(input("Выберете тип задачи: \n1. задача на информацию \n2. задача на звук \n3. задача на кодирование изображения \nВаш выбор: "))
if prob == 1:
    inf()
elif prob == 2:
    sound()
elif prob == 3:
    image()
