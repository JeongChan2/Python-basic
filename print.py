#separator 옵션
print('P','Y','T','H','O','N',sep='\t')
print('010','7777','1234',sep='-')
print('python','google.com',sep='@')

print()

#end 옵션
print('Welcome',end=' ')
print('IT News',end=' ')
print('Web Site')

print()

#file 옵션
import sys

print('Learn python',file=sys.stdout) # file에 쓰겠다.
print()

# format 사용(d : 3,s : 'python',f : 3.141592)
print('%s %s' %('one','two'))
print('{} {}'.format('one',2))    # 암묵적 {0} {1}
print('{1} {0}'.format('one','two'))

print('%10s' %('nice'))
print('{:>10}'.format('nice'))

print('%-10s' %('nice'))
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy')) #공간은 10개가있는데 왼쪽부터 5개만 출력