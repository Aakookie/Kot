def statistics():
    zabit = 0
    missed = 0
    team = input(f'Введите название страны, статистику которой хотите узнать: \n')
    team = team.lower()
    team_index = teams.index(team)
    team_score = score[team_index] # список
    for i in team_score:
        if i != '':
            zabit += int(i[0])
            missed += int(i[2])
    print(f'Забито мячей: {zabit} \nПропущено мячей: {missed}')

def team_results():
    team = input(f'Введите название страны, результаты которой хотите узнать: \n')
    team = team.lower()
    team_index = teams.index(team)
    team_score = score[team_index] # список
    for i in team_score:
        if i != '':
            print(f'{team.title()} VS {teams[team_score.index(i)].title()} - {i}')

def total_score():
    d_zabit = {}
    d_missed = {}
    sorted_d_zabit = {}
    sorted_d_missed = {}
    for i in score:
        zabit = 0
        missed = 0
        for s in i:
            if s != '':
                zabit += int(s[0])
                missed += int(s[2])
                # difference = abs(zabit - missed)
            d_zabit[teams[score.index(i)]] = zabit
            d_missed[teams[score.index(i)]] = missed
    sorted_z = sorted(d_zabit, key=d_zabit.get)  
    for w in sorted_z:
        sorted_d_zabit[w] = d_zabit[w]
    items = list(sorted_d_zabit.items())
    d_z = {k: v for k, v in reversed(items)}

    sorted_m = sorted(d_missed, key=d_missed.get)  
    for w in sorted_m:
        sorted_d_missed[w] = d_missed[w]
    items_1 = list(sorted_d_missed.items())
    d_m = {k: v for k, v in reversed(items_1)}
    print("Рейтинг лидеров по забитым мячам:")
    for key in d_z:
        print(str(key).title(), '-', d_z[key])
    print("Рейтинг лидеров по пропущенным мячам:")
    for key in d_m:
        print(str(key).title(), '-', d_m[key])
    
def main():
    choice = int(input('Приветствуем на групповом этапе Чемпионата мира по футболу 2022 в Катаре! \nКакую информацию вы хотите узнать? (Укажите номер выбранной позиции) \n1 - Статистику конкретной команды по забитым и пропущенным мячам \n2 - Результаты матчей конкретной команды \n3 - Общий рейтинг по забитым и пропущенным мячам \n4 - Узнать авторов \nВаш выбор: '))
    if choice == 1:
        statistics()
    if choice == 2:
        team_results()
    if choice == 3:
        total_score()
    if choice == 4:
        print("Над программой работали: \nПрограммист - Кукина Анна \nТестировщик - Козлова Карина")
    ans = int(input('Хотите узнать ещё что-нибудь? (0 - нет, 1 - да) \nВаш выбор: '))
    if ans == 1:
        main()
    else:
        print('Спасибо, что воспользовались этой программой!')

teams = ["нидерланды", "сенегал", "эквадор", "катар", "англия", "сша", "иран", "уэльс", "аргентина", "польша", "мексика", "саудовская аравия", "франция",  "австралия", "тунис", "дания", "япония", "испания", "германия", "коста-рика", "марокко", "хорватия", "бельгия",  "канада", "бразилия", "швейцария",  "камерун",  "сербия", "португалия", "южная корея",  "уругвай", "гана"]
score = [
    ['', '2:0', '1:1', '2:0'], # Нидерланды - 1
    ['0:2', '', '2:1', '3:1'], # Сенегал - 2
    ['1:1', '1:2', '', '2:0'], # Эквадор - 3
    ['0:2', '1:3', '0:2'], # Катар - 4
    ['', '', '', '', '', '0:0', '6:2', '3:0'], # Англия - 5 
    ['', '', '', '', '0:0', '', '1:0', '1:1'], # США - 6
    ['', '', '', '', '2:6', '0:1', '', '2:0'], # Иран - 7
    ['', '', '', '', '0:3', '1:1', '0:2'], # Уэльс - 8
    ['', '', '', '', '', '', '', '', '', '2:0', '2:0', '1:2'], # Аргентина - 9
    ['', '', '', '', '', '', '', '', '0:2', '', '0:0', '2:0'], # Польша - 10
    ['', '', '', '', '', '', '', '', '0:2', '0:0', '', '2:1'], # Мексика - 11
    ['', '', '', '', '', '', '', '', '2:1', '0:2', '1:2'], # Саудовская Аравия - 12
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '4:1', '0:1', '2:1'], # Франция - 13
    ['', '', '', '', '', '', '', '', '', '', '', '', '1:4', '', '1:0', '1:0'], # Австралия - 14
    ['', '', '', '', '', '', '', '', '', '', '', '', '1:0', '0:1', '', '0:0'], # Тунис - 15
    ['', '', '', '', '', '', '', '', '', '', '', '', '1:2', '0:1', '0:0'], # Дания - 16
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2:1', '2:1', '0:1'], # Япония - 17
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:2', '', '1:1', '7:0'], # Испания - 18
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:2', '1:1', '', '4:2'], # Германия - 19
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:0', '0:7', '2:4'], # Коста-Рика - 20
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:0', '2:0', '2:1'], # Марокко - 21
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:0', '', '0:0', '4:1'], # Хорватия - 22
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:2', '0:0', '', '1:0'], # Бельгия - 23
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:2', '1:4', '0:1'], # Канада - 24
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:0', '0:1', '2:0'], # Бразилия - 25
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:1', '', '1:0', '3:2'], # Швейцария - 26
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:0', '0:1', '', '3:3'], # Камерун - 27
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:2', '2:3', '3:3'], # Сербия - 28
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1:2', '2:0', '3:2'], # Португалия - 29
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2:1', '', '0:0', '2:3'], # Южная Корея - 30
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0:2', '0:0', '', '2:0'], # Уругвай - 31
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2:3', '3:2', '0:2'] # Гана - 32
    ]


main()

