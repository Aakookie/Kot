import random
eng = ['in course of', 'regurgitate', 'dispel', 'preconception', 'encounter', 'stigma', 'impair', 'fiercely', 'riot', 'to tackle', 'candid', 'designated']
rus = ['в процессе', "извергать", "развеять", "предубеждение", "сталкиваться", "клеймо", "испортить", "яростно", "бунтарь", "справиться", "искренний", "предназначенный"]
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
        print('Congratulations! You know the transltions of every given word')
        a = 1    
    
