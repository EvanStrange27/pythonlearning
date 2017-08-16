sum = 0
num = list(range(101))
for n in num:
    if n == 10:
        break
    sum = sum + n
    print(n,sum)
