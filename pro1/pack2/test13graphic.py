# Graphic 지원 모듈 사용 - turtle
# 사용할거라면 추가적인 공부 필요(우선 한번 해보는것에 의미를 둠)
from turtle import *
pen = Pen()

pen.color('red', 'yellow')
pen.begin_fill()

while True:
    pen.forward(200)
    pen.left(170)
    if abs(pen.pos()) < 1:
        break
pen.end_fill()
done()

