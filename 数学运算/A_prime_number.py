def is_prime(n):
    flag = True#此处可为多行函数定义代码
    for i in range(2,n):
        if n%i == 0:
            flag = False
            break
    return flag
ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i)== True:
        ls.remove(i)   #此处为一行代码
print(len(ls))
