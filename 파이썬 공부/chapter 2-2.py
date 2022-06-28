# id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(n) == id(m))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(n) == id(m))
print()

# 다양한 변수 선언
# Camel Case : numverOfCollegeFraduates  -> Method
# Pascal Case : NumverOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates (파이썬에서 많이 씀)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스) ; 시퀀스 - 반복처리 가능, 순서가 있는 것
set : 집합
dict : 사전
"""

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) x ** y -> 2 ** 3 #제곱
complex(3) ->복소수
a, b = divmod(100,8) -> 100을 8로 나누기, a = 몫, b = 나머지 저장
"""
#외부 모듈
import math
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 (반올림)
print(math.pi)

# 이스케이프 문자 사용
print("I'm Boy")
print('I\'m Boy')
print()

raw_s0 = "aaa \n aaaa"
print(raw_s0)
print()

# Row String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력 (다음라인에 무언가 연결이 된다)
multi_str = \
'''
문자열
멀티라인
테스트
'''
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "seoil Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print()

# 문자열 함수
"""
str_o1.capitalize : 첫 영어 대문자로
str_o1.endswith('s') : 끝 글자가 s 이냐
str_o1.replace("thon", 'Good') : 왼쪽 문자를 찾아서 오른쪽 문자로 바꿔주기
sorted(str_o1) : 리스트 형태로 반환 하면서 정렬
"""

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 시퀀스를 반복할 수 있다는 이야기
print()

# 슬라이싱
str_s1 = "Nice Python"
print(str_s1[1:9:2]) #세번째 인수는 단위
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드 (유니코드)
a = 'z'
print(ord(a))
print(chr(122))
