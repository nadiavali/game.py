import turtle

def square_man(t,x):
    for i in range (4):
        t.forward(x)
        t.left(90)

wn = turtle.Screen()
wn.bg.color('green')
wn.title('hey!')

alex= turtle.Turtle()
square_man(alex, 80)

wn.mainloop()
