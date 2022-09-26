p = int(input(f"p="))
Np = int(input(f"N{p}="))
k = 1
N10 = 0
while not Np == 0:
    N10 = N10 + (Np%10)*k
    k = k*p
    Np = Np//10
print(f"N10 = {N10}")