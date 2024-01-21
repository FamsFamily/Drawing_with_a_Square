import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.title("Drawing with a square: Plane")

t.speed(1)
t.shape("classic")
t.write("see the console")
fuselage=input("Enter the color of the fuselage: ")
plane_wing=input("Enter the color of the plane wing: ")
color=input("Enter a color: ")
speed=int(input("Enter the speed: "))
t.speed(speed)
t.shape("square")

def sfs(v):
    for i in range(v):
        t.stamp()
        t.forward(20)
    t.stamp()

#fuselage
t.color(fuselage)
t.pencolor("black")
t.up()
t.goto(0,120)
t.right(90)
sfs(11)
t.goto(20,100)
sfs(9)
t.goto(-20,100)
sfs(9)
t.color(plane_wing)
t.pencolor("black")

#plane wing
#main wing
t.goto(40,40)
t.left(90)
sfs(2)
t.goto(40,20)
sfs(3)
t.goto(40,0)
sfs(3)
t.goto(-40,40)
t.left(180)
sfs(2)
t.goto(-40,20)
sfs(3)
t.goto(-40,0)
sfs(3)
#addition wing
t.goto(40,-80)
t.stamp()
t.goto(-40,-80)
t.stamp()
t.goto(-20,-100)
sfs(2)
t.goto(20,-100)
t.left(180)
sfs(2)

#color
t.left(90)
t.color(color)
t.pencolor("black")
t.goto(0,0)
sfs(2)
t.goto(60,40)
sfs(1)
t.goto(-60,40)
sfs(1)

t.goto(-320,-140)
t.shape("classic")
t.color("black")
t.right(90)
t.write("Image Source: https://depositphotos.com/portfolio-66453848.html?content=vector&sh=c8b871d03bf55908df362327847384e57391e66f&qview=626351368")

turtle.done()
