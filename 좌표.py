import turtle as t
t.speed(5)

def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def txtwrite(x, y, text):
    t.up()
    t.goto(x, y)
    t.down()
    t.write(text)

def draw_xy(wsize, step, tx1, tx2):
    line(-wsize, 0, wsize, 0)
    line(0, -wsize, 0, wsize)

    for i in range(-wsize, wsize, step):
        line(i, -5, i, 5)
        if i != 0:
            txtwrite(i - 10, -20, tx1)
            tx1 = tx1 + 1

    for i in range(-wsize, wsize, step):
        line(-5, i, 5, i)
        if i != 0:
            txtwrite(20, i - 10, tx2)
            tx2 = tx2 + 1

wsize = 500
step = 100
tx1 = -4
tx2 = -4
draw_xy(wsize, step, tx1, tx2)

t.exitonclick()