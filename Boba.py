import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.title("Drawing with a square: Boba")

t.speed(1)
t.shape("classic")
t.write(" see the console")
cup=input("Enter the color of the cup:")
lid=input("Enter the color of the lid:")
straw=input("Enter the color of the straw:")
milk_tea=input("Enter the color of the milk tea:")
boba=input("Enter the color of the boba:")
speed=int(input("Enter the speed:"))
t.speed(speed)
t.shape("square")

def sfs(v):
    for i in range(v):
        t.stamp()
        t.forward(20)
    t.stamp()

#cup
t.color(cup)
t.pencolor("black")
t.up()
t.goto(-80,0)
sfs(1)
t.right(90)
sfs(6)
t.goto(-40,-140)
t.left(90)
sfs(4)
t.goto(60,-120)
t.left(90)
sfs(6)
t.right(90)
sfs(1)

#milk tea
t.color(milk_tea)
t.pencolor("black")
for i in range(7):
    t.goto(-40,-120+(20*i))
    sfs(4)

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
sfs(8)
t.goto(-60,40)
sfs(6)

#straw
t.color(straw)
t.pencolor("black")
t.goto(40,80)
t.left(180)
sfs(2)
t.left(90)
t.forward(20)
t.stamp()
t.forward(60)
sfs(4)

t.goto(-320,-180)
t.shape("classic")
t.color("black")
t.left(90)
t.write("Image Source: https://depositphotos.com/portfolio-66453848.html?content=vector&sh=a3d98026660e19099f1619e0009546c25a83946a&qview=626478118")

turtle.done()
