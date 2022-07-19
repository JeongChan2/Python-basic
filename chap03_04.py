# 리스트와 비교 중요
# 튜플 자료형(순서o 중복o 수정x 삭제x) # 불변

#선언
a = ()
b = (1)
print(type(a),type(b))
b = (1,)
print(type(b))
c = (11,12,13,14)
d = (100,1000,'Ace','Base','Captine')
e = (100,1000,('Ace','Base','Captine'))

print()
print('d - ', d[1])
print('e - ',list(e[-1][1]))

# d[0] = 1500  #error

#튜픓마수
a = (5,2,3,1,4)
print('a - ',a)
print('a - ',a.index(3)) #3이 있는 위치가 어딘지
print('a - ',a.count(2)) #2의 개수

# 팩킹 & 언팩킹

#팩킹
t = ('foo','bar','baz','qux')

# 언팩킹
(x1,x2,x3,x4) = t  #괄호가 있어도 되고 없어도 되는데 있는게 무언의 약속?
print(type(x1),type(x2),type(x3),type(x4))
print(x1,x2,x3,x4)

t2 = 1,2,3 #괄호가 없어도 튜플
t3 = 4,
x1,x3,x3 = t2
x4,x5,x6 = 4,5,6,7
print(type(x4))
