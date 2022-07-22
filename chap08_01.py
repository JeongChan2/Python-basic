# 파이썬 내장 함수
# 자주 사용한것 위주

# 절대값
# abs() 
from traceback import print_tb


print(abs(-3))

# all : iterable 요소 검사( 참, 거짓 )
print(all([1,2,3]))
print(all([1,2,0])) 
print(all([1,2,''])) #하나라도 false되는 요소를 가지고있으면 false출력

# any
print(any([1,2,3]))
print(any([1,2,0])) #하나라도 true가 되는 요소를 가지고 있으면 true출력 
# all : and       any : or 로 이해하면 편함

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + Iterable(반복 가능한) 객체 생성 
for i, name in enumerate(['abc','bcd','efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(filter(conv_pos, [1,-3,2,0,-5,6]))
print(list(filter(conv_pos, [1,-3,2,0,-5,6])))
#람다식
print(list(filter(lambda x: abs(x)>2,[1,-3,2,0,-5,6])))

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,7,6]))

# max, min : 최대,최소
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study')) # 현재 여기선 공백이 제일 작은값

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x: abs(x),[1,-3,2,0,-5,6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복 가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

for i in range(1,10):
    print(i,end=' ')
print()
print()

# round : 반올림
print(round(6.5781, 2))
print(round(5.6))
print(round(5.4))

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6,5,4,3,1,2]))
print(sorted("wefjiweofiaof"))

# sum : 반복가능한 개계(Iterable) 합 반환
print(sum([1,2,3,4,5,6,7,8,9,10]))
print(sum(range(1,101)))

# type : 자료형 
print(type(3))
print(type({}))
print(type({1,2}))
print(type(()))
print(type([]))

# zip : 반복 가능하능한 객체(Iterable) 의 요소를 묶어서 반환

print(list(zip([10,20,30],[40,50,60])))
print(list(zip([10,20,30],[40,50]))) #짝이 맞는것만 반환
print(type(list(zip([10,20,30],[40,50,60]))[0]))