#Functions 실습

# *args, **kwargs

#별표 하나는 튜플형태, 별표 두개는 딕셔너리 형태

# *agrs(언팩킹)
from audioop import mul


def args_func(*args): # 매개변수가 가변이다. 10개짜리, 10000개짜리가 넘어올수도있다.
    for i,v  in enumerate(args): # i는 index . v는 값 enumerate함수가 만들어주는 역할?
        print('Result : {} {}'.format(i,v))
    print('-----')

args_func('Lee')
args_func('Lee','Park')
args_func('Lee','Park','Kim')  #하나의 튜플 형태로 가정하겠다.


# **kwargs(언팩킹) #딕셔너리형이 넘어옴
def kwargs_func(**kwargs): # 위도 그렇고 매개변수명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("------")

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee',name2='Park')
kwargs_func(name1 = 'Lee',name2='Park',name3='Cho')

def example(args_1,args_2, *args, **kwargs):
    print(args_1,args_2,args,kwargs)

example(10,20,'Lee','Kim','Park',age1=20,age2=30,age3=40)


#중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)

# 실행불가
# func_in_func(100) 바깥에서 선언 불가

#람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

def mul_func(x,y):
    return x * y

lambda_mul_function = lambda x,y : x*y

print(mul_func(5,20))
print(lambda_mul_function(5,20))



def func_final(x,y,func):
    print(x*y*func(100,100))

print(func_final(10,20,lambda x,y : x*y)) #함수 넘기거나 람다함수를 넘기거나