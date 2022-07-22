# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time , random 등

import sys

from scipy import rand
print(sys.argv)

# (강제종료)
# sys.exit()

# 파이썬 패키지 위치
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# 쓰기
f = open("test.obj", "wb")
obj = {1: 'python', 2:'study', 3:'basic'}
pickle.dump(obj,f) # obj를 오픈한 파일 f 에 dump(쓴다)한다.
f.close()

# 읽기
f = open("test.obj", "rb")
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir(폴더 생성), rmdir(폴더 삭제) (비어있으면 삭제. 내용이 있으면 삭제되지않음), rename

import os
print(os.environ)
print(os.environ["USERNAME"])

# 현재 경로
print(os.getcwd())

print()
print()
# time : 시간 관련 처리
import time

print(time.time())
print(time.localtime(time.time()))
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print()

# 시간 간격 발생
for i in range(5):
    print(i)
    #time.sleep(1) # 1초 sleep

# random
import random

print(random.random()) # 0 ~ 1 실수
print(random.randint(1,45))
print(random.randrange(1,45))

# 섞기
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 무작위 선택
c = random.choice(d)
print(c)

# webbrowser : 본인 OS의 웹 브라우저 실행

import webbrowser

webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com")