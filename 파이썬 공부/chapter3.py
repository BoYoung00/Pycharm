# 리스트
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# 같은 id 값
temp = c
print(c == temp)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex) # 연장하다
print('a - ', a)

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)

# 딕셔너리
"""
a['name'] 키가 존재하지 않으면 에러
a.get('name') 키가 존재하지 않으면 None
"""