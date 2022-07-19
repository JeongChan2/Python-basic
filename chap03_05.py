#파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x , 키 중복 x , 수정o, 삭제o)

# a = () , [] , {}    #튜플, 리스트, 딕셔너리


# 선언
# a = {'name': 'Kim', 'name':'Lee'} #키 중복 허용 안됨
a = {'name': 'Kim', 'phone':'01012345678','birth':'870514'}
b = {0:'Hello'}
c = {'arr':[1,2,3,4]}
d = {
    'Name': 'NiceMan',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'Niceman')
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul'
)

# a = [f1,f2,f3]


print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


#출력
print('a - ', a['name']) # 존재x -> 에러발생
print('a - ', a.get('name1')) # None이라고 출력. 좀더 안전
print('b - ', b[0])
print('b - ', b.get(0))

print('f - ', f.get('City'))
print('f - ', f.get('Age'))


# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank']=[1,2,3]
print('a - ', a)

a[2]=[1,2]
print('a - ', a)

print('a - ',len(a)) # key의 개수

# dic_keys, dict_values, dict_items : (반복문(__iter__))에서 사용 가능

print('a - ',a.keys()) #키값들만
print('a - ', list(a.keys()))

print('a - ',a.values())
print('a - ', list(a.values()))

print('a - ', a.items())
print('a - ', list(a.items()))

print()

print('a - ',a.pop('name'))
print('a - ', a)

print()

print('f - ', f.popitem()) #임의로 하나 가져옴
print('f - ', f)

print()

print('a - ', 'birth' in a)