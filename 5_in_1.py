def hemming():
    a='0123456789'
    nums=list(a)
    print(nums)

    b='0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
      hem[i]=int(hem[i])
    print(hem)

    def distance(x,y):
      k = 7
      for i in range(7):
        if x % 10 == y % 10:
          k = k - 1
        x = x // 10
        y = y // 10
      return k

    cod = int(input("код = "))

    min = distance(cod,hem[0])
    imin = 0
    for i in range(10):
      D = distance(cod,hem[i])
      if D < min:
        min = D
        imin = i
    if min == 0:
      print(f"Код верный: символ {nums[imin]}")
    elif min==1:
      print(f"Код исправлен: символ {nums[imin]}")
    else:print(f"Код неверный")

def turn_into_10():
    p = int(input(f"Основание системы счисления = "))
    Np = int(input(f"Число, которое нужно перевести в {p} систему счисления= "))
    k = 1
    N10 = 0
    while not Np == 0:
        N10 = N10 + (Np%10)*k
        k = k*p
        Np = Np//10
    print(f"N10 = {N10}")

def from_10():
    N10 = int(input(f"Введите число в десятичной системе счисления = "))
    p = int(input(f"Введите основание системы счисления, в кторую нужно перевсети число = "))
    k = 1
    Np = 0
    while not N10==0:
        Np= Np + (N10 % p)*k
        k = k*10
        N10 = N10//p
    print(f"Np = {Np}")

def mult_table():
    p = int(input('Введите р (2<p,=10): '))
    print(f'{p} - ичная таблица умножения')
    for i in range(1, p):
        for j in range(1, p):
            z = (i*j//p)*10 + (i*j)%p
            print(z, end = ' ')
        print()

def morze():
    morse_d = {
    'а' : '.-',
    'б' : '-...',    
    'в' : '.--', 
    'г' : '--.', 
    'д' : '-..', 
    'е' : '.', 
    'ж' : '...-', 
    'з' : '--..', 
    'и' : '..', 
    'й' : '.---', 
    'к' : '-.-', 
    'л' : '.-..', 
    'м' : '--', 
    'н' : '-', 
    'о' : '---', 
    'п' : '.--.', 
    'р' : '.-.', 
    'с' : '...', 
    'т' : '-', 
    'у' : '..-', 
    'ф' : '..-.', 
    'х' : '....', 
    'ц' : '-.-.', 
    'ч' : '---.', 
    'ш' : '----', 
    'щ' : '--.-', 
    'ъ' : '.--.-', 
    'ы' : '-.--', 
    'ь' : '-..-', 
    'э' : '..-..', 
    'ю' : '..--', 
    'я' : '.-.-', 
    }

    w = input('Введите слово: ')
    ww = list(w)

    for i in ww:
        if i in morse_d.keys():
            znach = morse_d.get(i)
            print(znach, end = "|")

def main():
    choice = int(input('Выберите функцию: \n1. Код Хемминга \n2. Перевод числа в 10-ичную СС \n3. Перевод числа из 10-ичной СС \n4. Таблица умножения системы счисления \n5. Азбука Морзе \n--'))
    if choice == 1:
        hemming()
    if choice == 2:
        turn_into_10()
    if choice == 3:
        from_10()
    if choice == 4:
        mult_table()
    if choice == 5:
        morze()
main()