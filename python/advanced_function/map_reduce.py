# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    def cc(wudi):
       return reduce(fn, map(char2num, wudi))
    i =  s.index('.')
    left = s[:i]
    right = s[i+1:]
    return cc(left) + cc(right) / (10 ** len(right))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
