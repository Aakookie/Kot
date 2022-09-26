p = int(input('Введите р (2<p,=10): '))
print(f'{p} - ичная таблица умножения')
for i in range(1, p):
    for j in range(1, p):
        z = (i*j//p)*10 + (i*j)%p
        print(z, end = ' ')
    print()
    