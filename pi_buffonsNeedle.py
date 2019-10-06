# Buffon's Needle Approximate Pi

import turtle
import random
screen = turtle.Screen()
a = turtle.Turtle()
a.speed(0)

def buffonPi(num_needles):
    a.clear()
    drawLines()
    collisions = 0
    a.color('red')
    for i in range(num_needles):
        needle = randomNeedle()
        drawNeedle(needle)
        if isCollision(needle,a.pos()):
            collisions+= 1
    if (collisions>0):
        line_length = 100
        board_lines_spacing = 800 / 6
        pi = 2.00000*line_length*num_needles/(collisions * board_lines_spacing)
    else:
        pi = 0
    error = (3.14159-pi)/3.14159
    if (error<0):
        error *= -1
    print('%i of %i sticks crossed a line' % (collisions, num_needles))
    print('pi ~ %f, percent error = %f' % (pi,error))

def drawLines():
    a.color('black')
    global linexs
    distApart = 800/6
    a.up()
    a.goto(-400,-300)
    a.down()
    a.setheading(0)
    for edge in range(2):
        a.fd(800)
        a.lt(90)
        a.fd(600)
        a.lt(90)
    a.lt(180)
    a.fd(distApart)
    a.rt(90)
    for outer in range(2):
        a.fd(600)
        a.rt(90)
        a.fd(800+distApart*2)
        a.rt(90)
    a.up()
    a.setheading(90)
    linexs = [-400,400]
    for line in range(1,6):
        a.goto(-400+distApart*line,-300)
        linexs.append(-400+distApart*line)
        a.down()
        a.fd(600)
        a.up()

def randomNeedle():
    x,y = random.random()*800-400,random.random()*525-300
    direction = random.random()*360
    return (x,y,direction)

def drawNeedle(needle):
    a.up()
    a.goto(needle[0],needle[1])
    a.down()
    a.setheading(needle[2])
    a.fd(100)
    a.up()

def isCollision(needle,currentPos):
    for line in linexs:
        if needle[0]<line and currentPos[0]>line:
            return True
        if needle[0]>line and currentPos[0]<line:
            return True

again = 'Y'

while(again=='Y'):
    n = int(input('How many sticks would you like to drop?   '))
    buffonPi(n)
    again = (input('Again? (Y/N):   ')).upper()
