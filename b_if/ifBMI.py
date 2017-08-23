# -*- coding: utf-8 -*-

height = float(input('身高(m):'))
weight = float(input('体重(kg):'))
bmi = weight / (height * height)
print('你的BMI值为:%.1f，身体状况为:' % bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
elif bmi > 32:
	print('超重')
else:
	print('数值错误')
enter = input()