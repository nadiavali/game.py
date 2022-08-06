
import turtle

def square_drawing(t,s):
    for i in range(5):
        for i in range(4):
             t.forward(s)
             t.left(90)
        t.penup()
        t.forward(s+s)
        t.pendown()

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color('purple')
tess.speed(1)

square_drawing(tess, 20)

wn.mainloop()