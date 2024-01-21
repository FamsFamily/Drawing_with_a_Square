import turtle

c = turtle.Turtle()
c.shape("square")
c.speed(0)
c.up()

color = [
    ['black','dimgray','dimgrey','gray','grey','darkgray','darkgrey','silver','lightgray','lightgrey','gainsboro','whitesmoke','white','snow','rosybrown','lightcoral','indianred','brown','firebrick','maroon','darkred'],
    ['red','mistyrose','salmon','tomato','darksalmon','coral','orangered','lightsalmon','sienna','seashell','chocolate','saddlebrown','sandybrown','peachpuff','peru','linen','bisque','darkorange','burlywood','antiquewhite','tan'],
    ['navajowhite','blanchedalmond','papayawhip','moccasin','orange','wheat','oldlace','floralwhite','darkgoldenrod','goldenrod','cornsilk','gold','lemonchiffon','khaki','palegoldenrod','darkkhaki','ivory','beige','lightyellow','lightgoldenrodyellow','olive'],
    ['yellow','olivedrab','yellowgreen','darkolivegreen','greenyellow','chartreuse','lawngreen','honeydew','darkseagreen','palegreen','lightgreen','forestgreen','limegreen','darkgreen','green','lime','seagreen','mediumseagreen','springgreen','mintcream','mediumspringgreen'],
    ['mediumaquamarine','aquamarine','turquoise','lightseagreen','mediumturquoise','azure','lightcyan','paleturquoise','darkslategray','darkslategrey','teal','darkcyan','aqua','cyan','darkturquoise','cadetblue','powderblue','lightblue','deepskyblue','skyblue','lightskyblue'],
    ['steelblue','aliceblue','dodgerblue','lightslategray','lightslategrey','slategray','slategrey','lightsteelblue','cornflowerblue','royalblue','ghostwhite','lavender','midnightblue','navy','darkblue','mediumblue','blue','slateblue','darkslateblue','mediumslateblue','mediumpurple'],
    ['blueviolet','indigo','darkorchid','darkviolet','mediumorchid','thistle','plum','violet','purple','darkmagenta','fuchsia','magenta','orchid','mediumvioletred','deeppink','hotpink','lavenderblush','palevioletred','crimson','pink','lightpink']
]

print(len(color[0])+len(color[1])+len(color[2])+len(color[3])+len(color[4])+len(color[5])+len(color[6]))
for i in range(7):
    for j in range(21):
        c.goto(-650+(186*i),300-(30*j))
        c.color(color[i][j])
        c.pencolor("black")
        c.stamp()
        c.goto(-650+(186*i),295-(30*j))
        c.forward(20)
        c.write(color[i][j])
        #print(color[i][j])
c.goto(700,0)

turtle.done()