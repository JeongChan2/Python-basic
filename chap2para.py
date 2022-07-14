n = 700
print(n)
print(type(n))

#동시 선언
x = y = z = 700
print(x,y,z)

var = 75
var = "Change Value"
print(var)
print(type(var))
print()

# Object References
# 변수 값 할당 상태
print(300)
print(int(300))

print()

n = 777

print(n,type(n))
print()

m = n
print(m,type(m))
print()

m = 400
print(m)
print(m,type(m))
print()

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 544

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

m=800
n=800

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_collge_graduates

student_grade = 3