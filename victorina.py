import random
def vict():
    eng = ['in course of', 'regurgitate', 'dispel', 'preconception', 'encounter', 'stigma', 'impair', 'fiercely', 'riot', 'to tackle', 'candid', 'designated']
    rus = ['в процессе', "извергать", "развеять", "предубеждение", "сталкиваться", "клеймо", "испортить", "яростно", "бунтарь", "справиться", "искренний", "предназначенный"]
    string_e = '''enlightening_contemplate_to tolerate_interfere_affairs_tuition_fee'''
    string_r = '''вдохновляющий_созерцать_терпеть_вмешиваться_отношения_обучение_взнос'''
    new_e = string_e.split('_')
    new_r = string_r.split('_')
    #eng.extend(new_e)
    #rus.extend(new_r)
    #print(rus)
    print('Translate into Russian:')
    a = 0
    while a == 0:
        r = random.choice(eng)
        print(r)
        ans = input()
        if ans == rus[eng.index(r)]:
            print('You\'re right!')
            rus.pop(eng.index(r))
            eng.pop(eng.index(r))
        if len(eng) == 0:
            ans = input('Congratulations! You know the transltions of every given word \nDo you want to try again? \n(0 - no; 1 - yes) ')
            if ans == 1:
                vict()
            elif ans == 0:
                a = 1
                print('Have a good day!')
    
vict()
