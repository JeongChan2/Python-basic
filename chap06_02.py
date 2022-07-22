# 파이썬 모듈
# Module : 함수, 변수 ,클래스 등 파이썬 구성 요소 등을 모아놓은 파일

from re import sub


def add(x,y):
    return x + y

def substarct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print('-' * 15)
# print('called! innser!')
# print(add(5,5))
# print(substarct(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

#__name__ 사용
# 다른곳에서 import할때는 main이 아니기때문에 아래 내용이 실행이 되지않음
if __name__ =="__main__":
    print('-' * 15)
    print('called! __main__!')
    print(add(5,5))
    print(substarct(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15)

