import random
import os
import msvcrt

LEFT, DOWN, RIGHT, UP, END = ('LEFT', 'DOWN', 'RIGHT', 'UP', 'END')
arrow_keys = { #키보드 입력 값(확장자 b 포함)을 키 값으로 대응
b'w': UP,
b's': DOWN,
b'd': RIGHT,
b'a': LEFT,
b'0': END
}

row, col = (0,0) #전역 변수
puzzle = [] #2차원 리스트

#랜덤퍼즐 생성
def rand_puzzle():
    global puzzle, row, col
    arr = [i for i in range(row*col)] #씨드 리스트 1차원
    arr = random.sample(arr, row*col) #랜덤 샘플링

    for i in range(0, len(arr), col): #2차원으로 슬라이스
        puzzle.append(arr[i:i+col])

def prt_puzzle():
    for i in range(row):
        for j in range(col):
            if puzzle[i][j] == 0:
                print("    ", end='')
            else:
                print("%4d" %puzzle[i][j], end='')
        print()

def find_zero():
    for i in range(row):
        for j in range(col):
            if puzzle[i][j] == 0:
                return row*i+j

def check_complete():
    chk_cnt = 0
    for i in range(row):
        for j in range(col) :
            if puzzle[i][j] == (row * i + j + 1): chk_cnt += 1

    if chk_cnt >= (row * col - 1):
        return 1
    else:
        return 0

#메인시작
#변수 초기화
col=int(input("열 개수는? "))
row = col

rand_puzzle()
os.system('cls')
prt_puzzle()

def Left(r,c):
    if c+1 >= col:
        print("이동 불가")
    else:
        puzzle[r][c], puzzle[r][c + 1] = puzzle[r][c + 1], puzzle[r][c]

def Right(r,c):
    if c-1 < 0:
        print("이동 불가")
    else:
        puzzle[r][c], puzzle[r][c - 1] = puzzle[r][c - 1], puzzle[r][c]

def Down(r,c):
    if r-1 >= row:
        print("이동 불가")
    else:
        puzzle[r][c], puzzle[r - 1][c] = puzzle[r - 1][c], puzzle[r][c]

def Up(r,c):
    if r+1 < 0:
        print("이동 불가")
    else:
        puzzle[r][c], puzzle[r + 1][c] = puzzle[r + 1][c], puzzle[r][c]


os.system('cls')

#메인 시작
while True:
    zero_seq = find_zero()
    r = zero_seq // col #0의 행 위치
    c = zero_seq % row #0의 열 위치

    # key = input("a(좌) w(상) s(하) d(우) > ")
    print("a(좌) w(상) s(하) d(우) > ")
    ch = msvcrt.getch()

    if ch in arrow_keys.keys():
        key = arrow_keys[ch]
    else:
        key = 'Wrong'

    if key == LEFT:
        Left(r,c)
    elif key == RIGHT:
        Right(r,c)
    elif key == Up:
        Up(r,c)
    elif key == Down:
        Down(r,c)
    elif key == '0':
        print("End")
        break
    else:
        print("잘못된 키입니다")

    os.system('cls')
    prt_puzzle()

    if check_complete():
        print("성공")
        break