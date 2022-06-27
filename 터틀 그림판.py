import random
from turtle import *

def go(x,y): #마우스 클릭
    goto(x, y)

def east(): #오른쪽 방향키
    setheading(0)
    forward(10)

def north(): #위쪽 방향키
    setheading(90)
    forward(10)

def west(): #왼쪽 방향키
    seth(180)
    forward(10)

def south(): #아래쪽 방향키
    seth(270)
    forward(10)

def LClick(x, y):  # pendown 후 클릭된 좌표로 이동
    goto(x, y)


def RClick(x, y):  # penup 후 클릭된 위치로 이동
    penup()
    goto(x, y)
    pendown()

def CClick(x, y):  # 펜 색상 램덤색으로 변경
    r = random.random()
    g = random.random()
    b = random.random()
    pencolor((r, g, b))

hideturtle()
pensize(10)
pencolor("blue")
onscreenclick(go)

onkeypress(north, "Up")
onkeypress(south, "Down")
onkeypress(west, "Left")
onkeypress(east, "Right")
listen() #키 입력 대기기

onscreenclick(LClick, 1)		#Left 버튼(1) 클릭
onscreenclick(CClick, 2) 		#Center 버튼(2) 클릭
onscreenclick(RClick, 3) 		# Right 버튼(3) 클릭
done()