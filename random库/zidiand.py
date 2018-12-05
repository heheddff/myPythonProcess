import random
random.seed(0x1010)
encry = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*")
F = []
for i in range(10):
    ms = ''
    start = 0
    while start<10:
        k = random.randint(0,len(encry)-1)
        if start == 0:
            if k not in F:
                F.append(k)
            else:
                start = 0
                continue
        start+=1
        ms+=encry[k]            
    print(ms)
