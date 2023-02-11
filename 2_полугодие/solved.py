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

#16
sys.setrecurtionlimit()
def f(n):
    if n==1:
        return(1)
    else:
        return(n*f(n-1)):
    print(f(2023)/f(2020))
    
it1 = it2 = 1
for x1 in range(1, 2024):
    it1 = it1*x1
for x2 in range(1, 2021):
    it2 = it2*x2
print(it1/it2)

#17
x = [int(i) for i in f] # f - импортированный файл
a = []
b = [x for x in b if]

#23
def f(x, y):
    if x > y or x == 17:
        return(0)
    if x == y:
        return(1)
    return f(x+1, y) + f (x*2, y)
print(f(1, 10)*f(10, 35))
