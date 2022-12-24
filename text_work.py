with open('text1.txt') as f:
    n = f.readline()
    print(n)
with open('text1.txt') as f:
    n = f.readlines()
    print(n)
with open('text1.txt') as f:
    n = [x for x in f]
    print(n)
with open('text2.txt') as f1:
    m = f1.readline()
    print(m)
with open('text2.txt') as f1:
    m = f1.readlines() 
    print(m)
with open('text2.txt') as f1:
    m = [x for x in f1]
    print(m)
  
