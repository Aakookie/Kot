summ = 0
ss =[]
for i in range(500, 601):
    s_0 = str(i)[0]
    s_1 = str(i)[1]
    s_2 = str(i)[2]        
    sp = [int(s_0), int(s_1), int(s_2)]
    sp.sort() 
    if sp[0] != 0:
        max_n = int(f'{sp[2]}{sp[1]}')
        min_n = int(f'{sp[0]}{sp[1]}')
    elif sp.count(0) == 1:
        max_n = int(f'{sp[2]}{sp[1]}')
        min_n = int(f'{sp[1]}{sp[0]}')
    else:
        max_n = min_n = int(f'{sp[2]}{sp[1]}')
    if (max_n - min_n) == 10:
        ss.append(i)
        summ += i
print(ss)
print(summ)
