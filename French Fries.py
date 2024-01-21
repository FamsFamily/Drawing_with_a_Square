import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.title("Drawing with a Square: French Fries")

t.speed(1)
t.shape("classic")
t.write("see the console")
cup=input("Enter the color of the cup: ")
label=input("Enter the color of the label: ")
french_fries_1=input("Enter the color of the french fries 1: ")
french_fries_2=input("Enter the color of the french fries 2: ")
speed=int(input("Enter the speed: "))
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
sfs(10)
t.goto(0,-20)
sfs(10)
t.goto(0,-40)
sfs(10)
t.goto(20,-60)
sfs(8)
t.goto(20,-80)
sfs(8)
t.goto(20,-100)
sfs(8)
t.goto(40,-120)
sfs(6)

#label
t.color(label)
t.pencolor("black")
t.goto(60,-80)
sfs(4)
t.goto(80,-100)
sfs(2)

#french fries
#french fries 1
t.color(french_fries_1)
t.pencolor("black")
t.right(90)
t.goto(20,40)
sfs(2)
t.goto(60,60)
sfs(5)
t.goto(100,80)
sfs(6)
t.goto(140,60)
sfs(5)
t.goto(180,40)
sfs(2)
#french fries 2
t.color(french_fries_2)
t.pencolor("black")
t.goto(40,60)
sfs(4)
t.goto(80,80)
sfs(6)
t.goto(120,80)
sfs(6)
t.goto(160,60)
sfs(4)

t.goto(-320,-160)
t.shape("classic")
t.color("black")
t.left(90)
t.write("Image Source: https://depositphotos.com/portfolio-66453848.html?content=vector&sh=07666f49a53acfaa6aa00a995c102170eefd8a05&qview=626474916")

turtle.done()
