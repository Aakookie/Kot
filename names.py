from typing import Iterable
import random

vowels = 'аеёиоуыэюя'
double_vowels = 'еёяюи'
consonat = 'бвгджзйклмнпрстфхцчшщъь'


def test_for(subject: any,  filter_: Iterable, ttype: int) -> bool:
    """subject - Строка для проверки;
    filter_ - Фильтр по которому будет происходить проверка;
    ttype - Может принимать некоторые значения, соответствующие типу проверки
    1 - Если хоть 1 из subject содержится в filter_"""
    for i in filter_:
        match ttype:
            case 1:
                if i in subject:
                    return True, i
    return False, 1


def split_by_syllable(string: str) -> list[str]:
    ans = []
    add = True
    for i, v in enumerate(string):
        v = v.lower()
        if not add:
            if v in double_vowels and string[i-1] in 'ьъй':
                ans.append(v)
            else:
                ans[-1] += v
                if test_for(ans[-1], vowels, 1)[0] and i+1 < len(string) and test_for(string[i+1:], vowels, 1)[0] and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                    add = True
        else:
            ans.append(v)
            if test_for(ans[-1], vowels, 1)[0] and i+1 < len(string) and test_for(string[i+1:], vowels, 1)[0] and string[i+1] not in 'ьъ' and i+2 < len(string) and string[i+2] in vowels:
                add = True
            else:
                add = False
    return ans


def main():
    name = input('Введите ваше полное имя\n-> ')
    Name = split_by_syllable(name)
    # print(Name)
    for index, i in enumerate(Name):
        if test_for(i, consonat, 1)[0]:
            Name[index] = change_consonate(i)
        else:
            print(F'{i} не содержит')
    return ''.join(Name)

def change_consonate(slog:str):
        res = test_for(slog, consonat, 1)
        # print(res[1])
        return slog.replace(res[1], random.choice(consonat))

if __name__ == "__main__":
    while True:
        print(main())
        ans = input('Хотите узнать, кто работал над данной программой? (1 - да, !1 - нет) \nВаш ответ:')
        if ans == '1':
            print('Главный программист - Осипов Вячеслав \nОтветственные за дополнения - Иванов Николай, Балаганский Дмитрий \nПрограммист-консультант - Кукина Анна \nВеликий склейщик - Егоров Юрий \nМоральная поддержка - Козлова Карина')
        ans = input('Хотите попробовать ещё? (1 - да, !1 - нет)').strip()
        if ans != '1':
            break


