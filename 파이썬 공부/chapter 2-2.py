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
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)
