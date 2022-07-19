from audioop import mul
from glob import escape


str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))

str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))

# I'm Boy

print("I'm Boy")
print('I\'m Boy')
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

t_s1="Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

#멀티라인 입력
multi_str =\
'''
String
Multi line
Test'''
print(multi_str)

str_o1 = "python is python"
str_o2 = "AAA!"
str_o3 = "bbb"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

print()

#문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) #첫번째 문자를 대문자로
print("endswith?: ", str_o2.endswith("AA!")) #이 문자로 끝나니?
print("replace", str_o1.replace("thon", 'Good')) #이 부분을 찾아서 이걸로 바꿔줘
print("sorted: ", sorted(str_o1))
print ("split: ", str_o4.split(' '))

print()

# 반복(시퀸스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__ 라는게 있다. 그럼 반복사용가능

for i in im_str:
    print(i)

print()

str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3]) #0부터 3개만 나와라
print(str_s1[5:]) #[5:11]
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1)-1]) #str_s1[:10]
print(str_s1[0:8:2]) #0부터 8개인데 2칸씩 건너뛰어라
print(str_s1[-5:]) #음수
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드) 
a = 'z'
print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로

