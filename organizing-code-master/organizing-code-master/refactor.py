from turtle import *

speed(9)

def stripe(rectanglecolor):
    color(rectanglecolor)
    begin_fill()
    forward(300)
    left(90)
    forward(10)
    left(90)
    forward(300)
    left(90)
    forward(10)
    left(90)
    end_fill()

def move_next():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()




stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

stripe("white")
move_next()

stripe("red")
move_next()

penup()
goto(0, -60)
pendown()


color("blue")
begin_fill()
forward(100)
left(90)
forward(70)
left(90)
forward(100)
left(90)
forward(70)
left(90)
end_fill()


done()




