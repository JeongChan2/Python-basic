#집함(Set)
#집합(Set) 자료형(순서x , 중복x)

# 선언
a = set()
b = set([1,2,3,4,4,4,4])
c = set([1,4,5,6])
d = set([1,2,'Pen','Cap','Plate'])
e = {'foo','bar','baz','foo','qux'} # key없이 중괄호에 이런식으로 쓰면 set
f = {42, 'foo', (1,2,3), 3.141592}

print('a - ',type(a), a)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환 
l = list(c)
l2 = list(e)



# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))

print('s1 - s2',s1 -s2)
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))


#부분 집합 확인
print('subset', s2.issubset(s1))
print('superset', s1.issuperset(s2))


# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

s1.discard(3)    #discard 는 오류(예외)를 발생시키지 않음
print('s1 - ', s1)

s1.clear()
print('s1 - ', s1)

a = [1,2,3]
a.clear()
print('a - ', a)