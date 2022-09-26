N10 = int(input(f"N10 = "))
p = int(input(f"p = "))
k = 1
Np = 0
while not N10==0:
    Np= Np + (N10 % p)*k
    k = k*10
    N10 = N10//p
print(f"Np = {Np}")
