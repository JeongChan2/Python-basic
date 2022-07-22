# 파이썬 예외 처리
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다. 
# 3. 예외는 던져진다.
# 4. 예외 무시 할 수 있지만 하지말자

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim','Lee','Park']

try:
    z = 'Kim'
    x = name.index(z)
    print("{} Found it! {} in name".format(z ,x + 1))
except ValueError:
    print("Not found it! - Occurred ValueError!")
#except: 모든에러 다잡음
#except Exception: 동일
else:
    print('OK! else.')

print()


try:
    z = 'Cho'
    x = name.index(z)
    print("{} Found it! {} in name".format(z ,x + 1))
except Exception as e:
    print(e) #에러 내용이 나온다.
    print("Not found it! - Occurred ValueError!")
#except: 모든에러 다잡음
#except Exception: 동일
else:
    print('OK! else.')

print()


