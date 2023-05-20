#   s = []
#   for i in range(10, 1000001):
#       sum = 0
#       num = i
#       i = str(i)
#       am = len(i)
#       for j in i:
#           j = int(j)
#           sum += j**am
#       if sum == num:
#           s.append(num)
#   print(s)
#   key = 0
#   for m in s:
#       key += int(m)
#   print(key)

from itertools import product
summ = 0
maxi = 0
lis = [[0,712,673,1075,875,1622,423],[712, 0,1385, 1800, 1577, 2348, 1128],[673, 1385,0, 1499, 239, 2046, 244],[1075, 1800, 1499, 0,1287, 551, 1266],[875, 1577, 239, 1287,0, 1835, 442],[1622, 2348, 2046, 551, 1835,0, 1813],[423, 1128, 244, 1265, 442, 1813,0]]
way = product('0123456', repeat = 7)
st = '0123456'
for n in way:
    if all(n.count(a)==1 for a in st):
        summ = 0
        for i in range(len(n)-1):
            summ += lis[int(n[i])][int(n[i+1])]
        if summ > maxi:
            maxi = summ
print(maxi)

