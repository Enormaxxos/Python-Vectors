import tkinter
from Ball import Ball
from random import random,randrange
from math import pi

canvH = 800
canvW = 800

main = tkinter.Canvas(width=canvW,height=canvH,bg="black")
main.pack()

a = Ball(3)

balls = []

for i in range(10):
    balls.append(Ball(3))

def randomColor():
    choosing = "0123456789ABCDEF"
    final = "#"
    for i in range(6):
        index = randrange(0,16)
        final = final+choosing[index]
    return final

def draw():
    for a in balls:
        main.create_oval(a.pos.x-20,a.pos.y-20,a.pos.x+20,a.pos.y+20,fill=randomColor())
        a.update()
        a.vel.setHeading(random()*pi*2)

while True:
    draw()
    main.update()
    main.after(17)
    main.delete("all")

main.mainloop()

