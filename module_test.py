# 모듈 사용 실습

import sys

print(sys)
print(sys.path)
print(type(sys.path))

sys.path.append('c:\\math')
print(sys.path)

import test_module

print(test_module.power(10,3))

import chap06_02

print(chap06_02.add(10,10000))