import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.title("Drawing with a square: Boba")

t.speed(1)
t.shape("classic")
t.write("see the console")
cup=input("Enter the color of the cup:")
lid=input("Enter the color of the lid:")
straw=input("Enter the color of the straw:")
milk_tea=input("Enter the color of the milk tea:")
boba=input("Enter the color of the boba:")
speed=int(input("Enter the speed:"))
t.speed(speed)
t.shape("classic")
t.color(cup)
t.pencolor("black")
t.shape("square")
t.up()
def sfs():
    t.stamp()
    t.forward(20)
    t.stamp() 

def sfsfs():
    t.stamp()
    t.forward(20)
    t.stamp() 
    t.forward(20)
    t.stamp()

def sfsfsfsfs():
    t.stamp()
    t.forward(20)
    t.stamp() 
    t.forward(20)
    t.stamp()
    t.forward(20)
    t.stamp() 
    t.forward(20)
    t.stamp()


#cup
t.goto(-80,0)
sfs()
t.right(90)
t.forward(20)
sfsfs()
t.forward(20)
sfsfs()
t.goto(-40,-140)
t.left(90)
sfsfsfsfs()
t.goto(60,-120)
t.left(90)
sfsfs()
t.forward(20)
sfsfs()
t.forward(20)
t.right(90)
sfs()

#milk tea
t.color(milk_tea)
t.pencolor("black")
for i in range(7):
    t.goto(-40,-120+(20*i))
    sfsfsfsfs()

#boba
t.color(boba)
t.pencolor("black")
for i in range(3):
    t.goto(-40+(40*i),-120)
    t.stamp()
for i in range(2):
    t.goto(-40+(80*i),-80)
    t.stamp()

#lid
t.color(lid)
t.pencolor("black")
t.goto(-80,20)
sfsfsfsfs()
t.forward(20)
sfsfs()
t.forward(20)
t.stamp()
t.goto(-60,40)
sfsfsfsfs()
t.forward(20)
sfs()

#straw
t.color(straw)
t.pencolor("black")
t.goto(40,80)
t.left(180)
sfsfs()
t.left(90)
t.forward(20)
t.stamp()
t.forward(60)
sfsfsfsfs()
turtle.done()