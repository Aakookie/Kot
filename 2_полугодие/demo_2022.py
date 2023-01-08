for N in range(516): #5
  b = f'{N:b}
  if N % 2 == 0:
    b += '10'
  else:
    b = '1' + b + '01'
  if int(b, 2) > 516:
    print(N)
    break
    
for x in range(10000): #7
  s = x
  s = (s - 10) // 7
  n = 1
  while s > 0:
    n = n*2
    s = s - n 
  if n == 8:
    print(x)
    break
    
s = '8'*86
while '1111' in s or '8888' in s:
  if '1111' in s:
    s = s.replace('1111', '8', 1)
  else:
    s = s.replace('8888', '11', 1)
print(s)
