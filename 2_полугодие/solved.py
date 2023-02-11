#5
for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
#or
for N in range(516):
    b = f'{N:b}'
    if N % 2 == 0:
        b += '10'
    else:
        b = '1' + b + '01'
    if int(b, 2) > 516:
        print(N)
        break
#23
def f(x, y):
    if x > y or x == 17:
        return(0)
    if x == y:
        return(1)
    return f(x+1, y) + f (x*2, y)
print(f(1, 10)*f(10, 35))
