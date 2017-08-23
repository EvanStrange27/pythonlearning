def pass_seven(x=1,y=0):
    while y==0 or x <= y:
        z = str(x)
        s = 1
        for xyz in z:
            if xyz == '7' or x % 7 == 0:
                yield "过"
                break
            elif s == len(z):
                yield x
                break
            s = s + 1
        x = x + 1

for a in pass_seven(1,80):
    print(a)