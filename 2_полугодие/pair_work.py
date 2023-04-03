sp = [20, 2, 5, 5, 10, 0]
a = 1
while a == 1:
    for i in range(len(sp)-1):
        if sp[i] > sp[i+1]:
            sp.append(sp[i])
            sp.pop(i)
    if all(sp[j] <= sp[j+1] for j in range(len(sp)-1)):
        a = 0
    print(sp)