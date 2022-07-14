"""
int 정수
float 실수
complex 복소수
bool 불린
str 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
.
.
.
"""

# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0
int1 = 7
list = [str1,str2]

dict = {
    "name": "Machine Learning",
    "version": 2.0
} #key: value

print(list)
print()

print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float1))
print(type(int1))
print(type(dict))

tuple = (7,8,9)
tuple2 = 7,8,9
set = {7,8,9}

print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x ** y -> 2 ** 3 -> pow(2,3)
"""

i = 88
i2 = -14
big_int = 8888888888888812313131231321 # 가능

print(i)
print(i2)
print(big_int)
print(type(big_int))
print()


i1 = 39
i2 = 939
big_int1 = 1312313123123123123123133123
big_int2 = 39234892349284723947238942929
f1 = 1.234
f2 = 3.939
print("i1 + i2 : ",i1 + i2)



a = 3.
b = 6
c = .7
d = 12.7

print(type(a),type(b),type(c),type(d))
print(float(b))
print(int(c))
print(int(True))
print(complex(3))
print(complex('3')) #내부적으로 문자형 -> 숫자형
print(complex(False))

print(abs(-7))

print()

x,y=divmod(100,8)
print(x,y)

print(pow(5,3), 5**3)

print()

import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
