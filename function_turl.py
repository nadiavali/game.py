import turtle

def make_window(colr,ttl):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttl)
    return w

def make_turtle(colr, size, speed, shp):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(size)
    t.speed(speed)
    t.shape(shp)
    return t

wn = make_window('blue', 'I am learning')
tess = make_turtle('pink',2, 0, 'turtle')
man = make_turtle('red', 1,  3, 'arrow')

wn.mainloop()
