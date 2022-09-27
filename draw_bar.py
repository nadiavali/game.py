import tkinter
from turtle import *
xs = [48, 117, 200, 240, 160, 260, 220]
def draw_bar(t,height):
   t.begin_fill()
   t.left(90)
   t.forward(height)
   t.write('      ' + str(height))
   t.right(90)
   t.forward(60)
   t.right(90)
   t.forward(height)
   t.left(90)
   t.end_fill()
   t.forward(10)

wn = Screen()
wn.bgcolor('yellow')

tess = Turtle()
tess.pensize(7)
tess.color('blue','purple')
tess.speed(3)

for i in xs:
   draw_bar(tess, i)

wn.mainloop()