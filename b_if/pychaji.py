# -*- coding: utf-8 -*-

cjtable = {}
huanying = '欢迎使用《Py查绩》，'
goon = '\n已完成操作，接下来'
caidan = '''你可以：
1录入成绩 2查询成绩 3修改成绩 4关于本作 5退出 0菜单'''
caidanset = set([1,2,3,4,5,0])
#欢迎菜单
print(huanying,caidan)
caozuo = int(input('请输入数字进行操作：'))
#判断
panduan = caozuo in caidanset
if panduan == False:
    print('这个数字？不存在的，在下面重新输个')
    caozuo = 0
while caozuo != 5:
    #二次菜单
    if caozuo == 0:
        print(goon,caidan)
        caozuo = int(input('请输入数字进行操作：'))
        if panduan == False:
            print('这个数字？不存在的，在下面重新输个')
            caozuo = 0
        continue
    #录入
    if caozuo == 1:
        luru = input('\n姓名：')
        #判断
        panduan = luru in cjtable
        if panduan == True:
            jixu = input('已有此人信息，你确认要修改吗(Yes or No)：')
            if jixu == 'No':
                caozuo = 0
                continue
        cjtable[luru] = int(input('成绩：'))
        caozuo = 0
        continue
    #查询
    if caozuo == 2:
        chaxun = input('\n姓名：')
        #判断
        panduan = chaxun in cjtable
        if panduan == False:
            print('没有此条信息')
            caozuo = 0
            continue
        print('成绩：',cjtable[chaxun])
        caozuo = 0
        continue
    #修改
    if caozuo == 3:
        xiugai1 = input('\n姓名：')
        #判断
        panduan = xiugai1 in cjtable
        if panduan == False:
            print('没有此条信息')
            caozuo = 0
            continue
        xiugai2 = int(input('修改为：'))
        cjtable[xiugai1] = xiugai2 
        caozuo = 0
        continue
    #关于
    if caozuo == 4:
        print('\n没啥好说的，都散了吧，散了吧。')
        caozuo = 0
        continue