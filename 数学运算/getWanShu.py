for i in range(2,1001):
    su = 0
    for j in range(1,i):
        if i%j == 0:
            su+=j
    if i == su:
        print(i)
