# -*- coding: utf-8 -*-

# [s.lower() for s in L1]
# 使用内建的isinstance函数可以判断一个变量是不是字符串
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
# 期待输出: ['hello', 'world', 'apple']

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) == True]

print(L2)
enter = input()