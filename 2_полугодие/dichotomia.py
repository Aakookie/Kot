sp = [100, 98, 10, 8, 7, 5, 3, 11, 24, 35, 46, 57, 68, 69]
while len(sp) > 2:
    mid = len(sp)//2
    if sp[mid] > sp[mid-1]:
        sp = sp[:mid]
    else:
        sp = sp[mid:]
    print(sp)


