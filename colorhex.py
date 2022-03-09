import turtle
col=('red','yellow','green','cyan','pink','white')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(5)
for i in range(150):
    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)